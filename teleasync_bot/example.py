import os
import logging
import asyncio

from dotenv import load_dotenv
from teleasync import TelegramBot, EventRouter
from teleasync.objects import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

logging.basicConfig(level=logging.INFO)

bot = TelegramBot(token=os.getenv("BOT_TOKEN"))

router = EventRouter()


@router.command("start")
async def start_command(message):
    first_name = message.from_.first_name
    last_name = message.from_.last_name or ""

    await bot.send_sticker(
        chat_id=message.chat.id,
        sticker_="CAACAgIAAxkBAAEHlExqzib8USssEfaQmInv9hk5ApUDIgACAQEAAladvQoivp8OuMLmND0E"
    )

    inline_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📚 Documentation", url="https://teleasync.readthedocs.io"),
                InlineKeyboardButton(text="⭐ GitHub Repository", url="https://github.com/kazaryanarmen/teleasync")
            ]
        ]
    )

    await bot.send_message(
        chat_id=message.chat.id,
        text=f"""<b>Hello</b>, <code>{first_name} {last_name}</code>!

This is a test Telegram bot for the <b>teleasync</b> Python library.

This bot processes standard HTTP requests and sends them to the Bot API server, directly using the <b>teleasync</b> library.

To get the available commands, enter /help.""",
        parse_mode="HTML",
        reply_markup=inline_keyboard
    )


@router.command("help")
async def help_command(message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="""<b>Available Commands:</b>

/start - Start the bot and get greeting
/help - Show this help message""",
        parse_mode="HTML"
    )


async def main():
    await bot.start_polling_from(router)


if __name__ == "__main__":
    asyncio.run(main())