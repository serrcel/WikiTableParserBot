from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from database import session
from city import City

btn_parse = KeyboardButton("Спарсить города 👆")
btn_find = KeyboardButton("Найти город 🏙")

menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(btn_parse, btn_find)

city_callback = CallbackData("Cities", "page")


def get_fruits_keyboard(page: int = 0) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    city_list = session.query(City).all()
    has_next_page = len(city_list) > page + 1

    if page != 0:
        keyboard.add(
            InlineKeyboardButton(
                text="< Назад",
                callback_data=city_callback.new(page=page - 1)
            )
        )

    keyboard.add(
        InlineKeyboardButton(
            text=f"• {page + 1}",
            callback_data="dont_click_me"
        )
    )

    if has_next_page:
        keyboard.add(
            InlineKeyboardButton(
                text="Вперёд >",
                callback_data=city_callback.new(page=page + 1)
            )
        )

    return keyboard