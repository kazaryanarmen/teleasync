# TeleAsync

[![PyPI version](https://img.shields.io/pypi/v/teleasync.svg)](https://pypi.org/project/teleasync)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-10.3-blue?logo=telegram&logoColor=white)](https://core.telegram.org/bots/api)


**teleasync** is a simple asynchronous Telegram Bot API library in Python.

---

## 🚀 Installation

From PyPI:
```bash
pip install teleasync
```

From GitHub:
```bash
pip install git+https://github.com/kazaryanarmen/teleasync.git
```

---

## 💡 Example code
Create a simple Telegram Bot in just a few minutes:

```python
from teleasync import TelegramBot, EventRouter
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

bot = TelegramBot(token="BOT_TOKEN")

router = EventRouter()

@router.message()
async def receive_messages(message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"You said {message.text}"
    )

async def main():
    await bot.start_polling_from(router)

if __name__ == "__main__":
    asyncio.run(main())
```

or the example is available in the `teleasync_bot/` folder in the [GitHub](https://github.com/kazaryanarmen/teleasync) repository.