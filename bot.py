from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)

# Tokenni Railway variables orqali olish
TOKEN = os.getenv("BOT_TOKEN")

# Bot va dispatcher yaratish
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# /start komandasi
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Salom! Men Railway’da ishlayapman 🎉")

# Boshqa barcha xabarlarga javob
@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

# Botni ishga tushirish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
