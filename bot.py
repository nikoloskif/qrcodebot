from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
import asyncio
import qrcode
from config import Config, load_config

config: Config = load_config()
BOT_TOKEN: str = config.tg_bot.token

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher()

async def launch(message: Message):
    await message.answer('Hi, I am a QR code bot.\nSend me any text and I will create a QR code for you')

async def helper(message: Message):
    await message.answer('If there is a problem, write to me: https://t.me/alexkiff')

async def donation(message: Message):
    img1 = FSInputFile('donate.jpeg')
    await message.reply_photo(img1, caption = f'EQBh-O6xVjSn6r36xyXqmu8F342KoT729u_N4facSTabZLT2\n\nSend only Toncoin (TON) to this address.\nSending other coins may result in permanent loss!')

async def send_qr(message: Message):
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=16,
        border=2)

    qr.add_data(message.text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('picture.png')
    img = FSInputFile('picture.png')
    await message.reply_photo(img, caption = f'QR code successfully generated.\n\nThis bot is absolutely free.\nAt the same time, you can support its development with a donation by typing the command /donate')

dp.message.register(launch, Command(commands=['start']))
dp.message.register(helper, Command(commands=['help']))
dp.message.register(donation, Command(commands=['donate']))
dp.message.register(send_qr)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())