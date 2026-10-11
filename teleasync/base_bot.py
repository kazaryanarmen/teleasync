from __future__ import annotations
import asyncio
import json
import logging
import re

import httpx

from .exceptions import (
    TelegramAPIError,
    TelegramBadRequestError,
    TelegramNetworkError,
    TelegramUnauthorizedError,
)
from .objects.input_file import InputFile

logger = logging.getLogger("teleasync")

_TOKEN_RE = re.compile(r"/bot\d+:[\w-]+/")


class _HideToken(logging.Filter):
    """Маскирует токен бота в логах httpx (он входит в URL запроса)."""

    def filter(self, record):
        try:
            message = record.getMessage()
        except Exception:
            return True
        record.msg = _TOKEN_RE.sub("/bot<hidden>/", message)
        record.args = ()
        return True


logging.getLogger("httpx").addFilter(_HideToken())

# Параметры, которые Telegram ждёт под их собственным именем, а не как attach://
DIRECT_FILE_KEYS = {"certificate"}


class BaseBot:
    def __init__(self, token: str, client: httpx.AsyncClient | None = None):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{token}"
        self.file_url = f"https://api.telegram.org/file/bot{token}"
        self._client = client
        self._owns_client = client is None

    async def get_client(self) -> httpx.AsyncClient:
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(timeout=60.0)
            self._owns_client = True
        return self._client

    async def aclose(self) -> None:
        """Закрывает HTTP-клиент. Не путать с Telegram API методом close()."""
        if self._owns_client and self._client and not self._client.is_closed:
            await self._client.aclose()

    @staticmethod
    def _attach(value, inputs: dict):
        """Рекурсивно заменяет InputFile на attach://имя и складывает файл в inputs."""
        if isinstance(value, InputFile):
            name = f"attach_{len(inputs)}"
            inputs[name] = value
            return f"attach://{name}"
        if hasattr(value, "to_dict"):
            value = value.to_dict()
        if isinstance(value, list):
            return [BaseBot._attach(i, inputs) for i in value]
        if isinstance(value, dict):
            return {k: BaseBot._attach(v, inputs) for k, v in value.items()}
        return value

    async def request(self, method_name: str, params: dict | None = None, files: dict | None = None):
        url = f"{self.base_url}/{method_name}"
        params = dict(params or {})
        inputs: dict[str, InputFile] = {}   # имя multipart-поля -> файл

        # files от сгенерированных методов: InputFile / bytes / file_id / объект (InputSticker...)
        for key, value in (files or {}).items():
            if value is None:
                continue
            if isinstance(value, InputFile):
                inputs[key] = value
            elif isinstance(value, (bytes, bytearray)) or hasattr(value, "read"):
                inputs[key] = InputFile(value)
            else:
                params[key] = value          # str (file_id/URL) или объект с to_dict

        cleaned = {}
        for k, v in params.items():
            if v is None:
                continue
            if isinstance(v, InputFile) and k in DIRECT_FILE_KEYS:
                inputs[k] = v
                continue
            cleaned[k] = self._attach(v, inputs)

        multipart = bool(inputs)
        if multipart:
            # в multipart вложенные структуры должны быть JSON-строкой
            for k in list(cleaned):
                if isinstance(cleaned[k], (dict, list)):
                    cleaned[k] = json.dumps(cleaned[k])

        client = await self.get_client()
        try:
            if multipart:
                real_files = {name: f.to_httpx() for name, f in inputs.items()}
                response = await client.post(url, data=cleaned, files=real_files)
            else:
                response = await client.post(url, json=cleaned)
        except httpx.RequestError as e:
            raise TelegramNetworkError(f"Network error during request to {method_name}: {e!r}")
        finally:
            for f in inputs.values():
                f.close()

        try:
            data_json = response.json()
        except Exception:
            raise TelegramAPIError(f"Invalid JSON response (HTTP {response.status_code})")
        logger.debug("API [%s] -> %s", method_name, data_json)

        if not isinstance(data_json, dict):
            raise TelegramAPIError(f"Unexpected response format: {data_json!r}")

        if not data_json.get("ok", False):
            code = data_json.get("error_code")
            desc = data_json.get("description", "Unknown error")
            if code == 401:
                raise TelegramUnauthorizedError(f"Authorization error: {desc}", code)
            if code == 400:
                raise TelegramBadRequestError(f"Bad request: {desc}", code)
            err = TelegramAPIError(f"API error [{code}]: {desc}", code)
            err.retry_after = (data_json.get("parameters") or {}).get("retry_after")
            raise err

        return data_json.get("result")

    async def download_file(self, file_path: str, destination_path: str) -> None:
        url = f"{self.file_url}/{file_path}"
        client = await self.get_client()
        try:
            async with client.stream("GET", url) as response:
                if response.status_code != 200:
                    raise TelegramAPIError(f"Failed to download file. Status code: {response.status_code}")
                with open(destination_path, "wb") as f:
                    async for chunk in response.aiter_bytes(chunk_size=8192):
                        f.write(chunk)
        except httpx.RequestError as e:
            raise TelegramNetworkError(f"Network error while downloading file: {e!r}")

    @staticmethod
    def _update_key(update: dict):
        """Ключ для сохранения порядка: апдейты одного чата идут строго по очереди."""
        for name, value in update.items():
            if name == "update_id" or not isinstance(value, dict):
                continue
            chat = value.get("chat") or (value.get("message") or {}).get("chat")
            if chat and chat.get("id") is not None:
                return chat["id"]
            sender = value.get("from")
            if sender and sender.get("id") is not None:
                return sender["id"]
        return ("update", update.get("update_id"))

    async def _process_update(self, router, update: dict, sem: asyncio.Semaphore, locks: dict) -> None:
        key = self._update_key(update)
        entry = locks.get(key)
        if entry is None:
            entry = locks[key] = [asyncio.Lock(), 0]
        entry[1] += 1
        try:
            async with entry[0]:
                await router.feed(update)
        except asyncio.CancelledError:
            raise
        except Exception:
            logger.exception("Update %s failed", update.get("update_id"))
        finally:
            entry[1] -= 1
            if entry[1] == 0:
                locks.pop(key, None)
            sem.release()

    async def start_polling_from(self, router, interval: float = 1.0, concurrency: int = 1) -> None:
        """concurrency — сколько апдейтов обрабатывается одновременно (1 = строго по очереди).
        При concurrency > 1 апдейты одного чата всё равно обрабатываются по порядку."""
        offset = 0
        backoff = interval
        bot_username = "Unknown Bot"
        sem = asyncio.Semaphore(max(1, concurrency))
        locks: dict = {}
        tasks: set[asyncio.Task] = set()

        try:
            await self.delete_webhook()  # иначе 409, если раньше стоял webhook
            me = await self.get_me()
            if isinstance(me, dict) and me.get("username"):
                bot_username = f"@{me['username']}"
        except TelegramUnauthorizedError:
            logger.critical("Invalid bot token")
            await self.aclose()
            raise
        except Exception:
            logger.exception("Startup check failed")

        logger.info("\n%s", "-" * 50)
        logger.info("Bot [%s] started!", bot_username)
        logger.info("Polling for updates... (Press CTRL+C to stop)")
        logger.info("%s\n", "-" * 50)

        try:
            while True:
                try:
                    updates = await self.get_updates(offset=offset, timeout=30)
                    backoff = interval

                    for update in updates or []:
                        offset = update["update_id"] + 1
                        await sem.acquire()   # ограничение параллельности
                        task = asyncio.create_task(self._process_update(router, update, sem, locks))
                        tasks.add(task)
                        task.add_done_callback(tasks.discard)

                except asyncio.CancelledError:
                    raise
                except TelegramUnauthorizedError:
                    logger.critical("Invalid bot token, stopping")
                    raise
                except TelegramAPIError as e:
                    delay = getattr(e, "retry_after", None) or backoff
                    logger.error("API error: %s (retry in %.1fs)", e, delay)
                    await asyncio.sleep(delay)
                    backoff = min(backoff * 2, 30)
                except Exception:
                    logger.exception("Polling error, retry in %.1fs", backoff)
                    await asyncio.sleep(backoff)
                    backoff = min(backoff * 2, 30)
        finally:
            if tasks:
                _, pending = await asyncio.wait(list(tasks), timeout=5)
                for t in pending:
                    t.cancel()
                if pending:
                    await asyncio.gather(*pending, return_exceptions=True)
            await self.aclose()
            logger.info("\n%s", "-" * 50)
            logger.info("Polling for [%s] stopped gracefully. Goodbye!", bot_username)
            logger.info("%s", "-" * 50)