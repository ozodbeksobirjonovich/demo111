import logging
from aiogram import Bot, Dispatcher, executor, types
from pytube import YouTube

# Bot tokeningizni bu yerga qo'ying
API_TOKEN = '7944663340:AAHRLAaEXCfvHUQAhDoWBd_yJpbOIcHKLJU'

# Loggingni sozlash
logging.basicConfig(level=logging.INFO)

# Bot va Dispatcherni yaratish
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# /start buyrug'ini qabul qiluvchi handler
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum! YouTube videosini yuklab olish uchun menga video linkini yuboring.")

# Har qanday matn xabarni qabul qiluvchi handler
@dp.message_handler()
async def download_video(message: types.Message):
    try:
        # YouTube obyektini yaratish
        yt = YouTube(message.text)

        # Eng yuqori sifatli videoni olish
        stream = yt.streams.get_highest_resolution()

        # Videoni yuklab olish
        await message.reply("Videoni yuklab olish boshlandi...")
        stream.download()
        await message.reply("Video muvaffaqiyatli yuklab olindi!")

    except Exception as e:
        await message.reply(f"Xatolik yuz berdi: {e}")

# Botni ishga tushirish
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
