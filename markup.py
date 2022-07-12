from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


btn_parse = KeyboardButton("Спарсить города 👆")
btn_find = KeyboardButton("Найти город 🏙")
btn_find_city = KeyboardButton("Найти 🔎")

menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_parse, btn_find)
find_city_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_find_city)