import os
import asyncio
from aiogram import Bot, Dispatcher
from handlers.main import register_handlers

BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Error: BOT_TOKEN is not set in environment variables.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

async def main():
    try:
        print("Starting bot...")
        await dp.start_polling()
    finally:
        await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
