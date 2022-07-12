from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types


API_TOKEN = TOKEN

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

