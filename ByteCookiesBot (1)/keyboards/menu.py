from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("🛒 Каталог"))
    kb.add(KeyboardButton("📦 Мои заказы"))
    return kb