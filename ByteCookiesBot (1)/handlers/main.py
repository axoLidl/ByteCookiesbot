from aiogram import types, Dispatcher
from keyboards.menu import main_menu
from utils.config import ADMIN_ID

async def start_command(message: types.Message):
    await message.answer("Добро пожаловать в магазин!", reply_markup=main_menu())

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])