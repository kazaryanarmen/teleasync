from __future__ import annotations
import asyncio
import inspect
import json
import logging
import re

from .objects.update import Update

logger = logging.getLogger("teleasync.router")

UPDATE_EVENTS = (
    "message", "edited_message", "channel_post", "edited_channel_post",
    "business_connection", "business_message", "edited_business_message",
    "deleted_business_messages", "guest_message", "message_reaction",
    "message_reaction_count", "inline_query", "chosen_inline_result",
    "callback_query", "shipping_query", "pre_checkout_query",
    "purchased_paid_media", "poll", "poll_answer", "my_chat_member",
    "chat_member", "chat_join_request", "chat_boost", "removed_chat_boost",
    "managed_bot", "subscription", "stopped_message_generation",
)
# События, чей объект — Message (для них доступны фильтры сообщений)
MESSAGE_EVENTS = {
    "message", "edited_message", "channel_post", "edited_channel_post",
    "business_message", "edited_business_message", "guest_message",
    "successful_payment",
}


def _as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return list(value)
    return [value]


def _is_async(handler) -> bool:
    return (inspect.iscoroutinefunction(handler)
            or inspect.iscoroutinefunction(getattr(handler, "__call__", None)))


async def _run_handler(handler, *args, **kwargs):
    """async-хендлеры выполняются в цикле, обычные — в потоке (не блокируют бота).
    Обычный хендлер не должен обращаться к event loop (await, create_task)."""
    if _is_async(handler):
        return await handler(*args, **kwargs)
    result = await asyncio.to_thread(handler, *args, **kwargs)
    if inspect.isawaitable(result):
        result = await result
    return result


def _message_filter(*, content_types=None, text=None, startswith=None, regex=None,
                    chat_types=None, ignore_commands=False):
    types = _as_list(content_types)
    texts = _as_list(text)
    prefixes = tuple(_as_list(startswith))
    chats = _as_list(chat_types)
    pattern = re.compile(regex) if isinstance(regex, str) else regex

    def check(m) -> bool:
        if chats and getattr(getattr(m, "chat", None), "type", None) not in chats:
            return False
        if types and not any(getattr(m, t, None) for t in types):
            return False
        body = getattr(m, "text", None) or getattr(m, "caption", None) or ""
        if ignore_commands and body.startswith("/"):
            return False
        if texts and getattr(m, "text", None) not in texts:
            return False
        if prefixes and not (getattr(m, "text", None) or "").startswith(prefixes):
            return False
        if pattern and not pattern.search(body):
            return False
        return True

    return check


def _callback_filter(*, data=None, startswith=None, regex=None):
    datas = _as_list(data)
    prefixes = tuple(_as_list(startswith))
    pattern = re.compile(regex) if isinstance(regex, str) else regex

    def check(q) -> bool:
        value = getattr(q, "data", None) or ""
        if datas and value not in datas:
            return False
        if prefixes and not value.startswith(prefixes):
            return False
        if pattern and not pattern.search(value):
            return False
        return True

    return check


class EventRouter:
    """Фильтры (все необязательные, комбинируются через И):

    @router.message(content_types=["photo"], chat_types="private")
    @router.message(text="привет")  /  startswith="!"  /  regex=r"^\\d+$"  /  ignore_commands=True
    @router.callback_query(data="ping")  /  startswith="page:"  /  regex=...
    @router.command("start", chat_types="private")
    Любой декоратор принимает func=<предикат(obj) -> bool>.
    """

    def __init__(self):
        self._handlers: dict[str, list] = {ev: [] for ev in UPDATE_EVENTS}
        self._handlers["successful_payment"] = []
        self.command_handlers: dict[str, list] = {}

    # ---------- регистрация ----------
    @staticmethod
    def _build_checks(builder, filters: dict) -> list:
        filters = dict(filters)
        predicate = filters.pop("func", None)
        checks = []
        if filters:
            if builder is None:
                raise TypeError(f"Для этого события нет фильтров: {sorted(filters)}")
            checks.append(builder(**filters))
        if predicate is not None:
            checks.append(predicate)
        return checks

    @staticmethod
    def _wrap(handler, checks: list):
        if not checks:
            return handler

        async def wrapper(obj, *args, **kwargs):
            for check in checks:
                result = check(obj)
                if inspect.isawaitable(result):
                    result = await result
                if not result:
                    return None
            return await _run_handler(handler, obj, *args, **kwargs)

        wrapper.__name__ = getattr(handler, "__name__", "handler")
        return wrapper

    def _make_decorator(self, event: str, builder, filters: dict):
        checks = self._build_checks(builder, filters)

        def decorator(handler):
            self._handlers[event].append(self._wrap(handler, checks))
            return handler
        return decorator

    def command(self, commands: str | list[str], **filters):
        names = [c.lstrip("/").lower() for c in _as_list(commands)]
        checks = self._build_checks(_message_filter, filters)

        def decorator(handler):
            wrapped = self._wrap(handler, checks)
            for name in names:
                self.command_handlers.setdefault(name, []).append(wrapped)
            return handler
        return decorator

    # ---------- выполнение ----------
    async def _execute_handler(self, handler, *args, **kwargs):
        try:
            return await _run_handler(handler, *args, **kwargs)
        except Exception:
            logger.exception("Handler %s failed", getattr(handler, "__name__", repr(handler)))

    async def _handle_message(self, message) -> None:
        text = getattr(message, "text", None) or getattr(message, "caption", None) or ""
        if text.startswith("/"):
            name = text.split(maxsplit=1)[0][1:].lower().split("@")[0]
            for handler in list(self.command_handlers.get(name, [])):
                await self._execute_handler(handler, message)

        for handler in list(self._handlers["message"]):
            await self._execute_handler(handler, message)

        if getattr(message, "successful_payment", None):
            for handler in list(self._handlers["successful_payment"]):
                await self._execute_handler(handler, message)

    async def feed(self, update_data: dict | str | list) -> None:
        if isinstance(update_data, list):
            for item in update_data:
                await self.feed(item)
            return

        if isinstance(update_data, str):
            update_data = json.loads(update_data)

        update = Update.from_dict(update_data)
        if not update:
            return

        if update.message:
            await self._handle_message(update.message)

        for event in UPDATE_EVENTS:
            if event == "message":
                continue
            obj = getattr(update, event, None)
            if obj:
                for handler in list(self._handlers[event]):
                    await self._execute_handler(handler, obj)


def _make_event_decorator(event: str):
    if event in MESSAGE_EVENTS:
        builder = _message_filter
    elif event == "callback_query":
        builder = _callback_filter
    else:
        builder = None

    def method(self, **filters):
        return self._make_decorator(event, builder, filters)

    method.__name__ = event
    method.__doc__ = f"Регистрирует хендлер события '{event}'."
    return method


for _event in UPDATE_EVENTS + ("successful_payment",):
    setattr(EventRouter, _event, _make_event_decorator(_event))