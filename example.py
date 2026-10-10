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