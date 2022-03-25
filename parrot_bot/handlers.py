import analizator
from main import bot, dp
from analizator import *
from aiogram.types import Message
from config import admin_id

async def send_to_admin(dp):
    await bot.send_message(admin_id,"Бот запущен")

@dp.message_handler()
async def echo(message: Message):

    mastext=analizator.jhn_analizator(message.text)
    for tx in mastext:
        await message.reply(tx)