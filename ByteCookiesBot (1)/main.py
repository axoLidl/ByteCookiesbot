from aiogram import Bot, Dispatcher, executor, types
from handlers.main import register_handlers
from utils.config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)