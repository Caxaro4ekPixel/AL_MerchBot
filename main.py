from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from decouple import config

bot = Bot(token=config('TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton('Посмотреть', web_app=WebAppInfo(url='https://caxaro4ekpixel.github.io/AL_MerchBot/')))
    await message.answer('Привет! Я бот, который поможет тебе найти и купить мерч', reply_markup=markup)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
