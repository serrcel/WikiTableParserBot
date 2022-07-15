import logging
from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
import markup as menu
import parser

API_TOKEN = TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Привет, я бот-парсер и я помогу получить список городов!", reply_markup=menu.menu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Найти город 🏙':
        await message.reply("Введите название города или его часть")
    elif message.text == 'Спарсить города 👆':
        parser.parse_page()
        await message.reply("Получен список городов")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)