from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)

TOKEN = "7911558762:AAH-OVtm3iE40WAIUPquuBsI30ZBNTjALhw"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# /start komandasi
@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await message.answer("Salom! Men Railway’da ishlayapman 🎉")

# Boshqa barcha matnlarga javob
@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(f"Siz yozdingiz: {message.text}")

# Ishga tushirish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
