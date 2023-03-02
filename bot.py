
import requests as requests
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, URLInputFile
from environs import Env

env = Env()
env.read_env()

API_TOKEN: str = env('BOT_TOKEN')

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет!')


@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе картинку')


@dp.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')


@dp.message()
async def send_echo(message: Message):
    response = requests.get('https://picsum.photos/1200/800')
    await message.answer_photo(URLInputFile(response.url), caption='Случайное фото')


if __name__ == '__main__':
    dp.run_polling(bot)
