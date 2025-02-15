import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message

logging.basicConfig(level=logging.INFO)
bot = Bot(token='7759664843:AAGjRGBIIvwtD0CGkF1m-y-U5DWqjHKsbwE')
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_name(message: Message):
    await message.answer("Hello, world")

@dp.message(Command("info"))
async def cmd_name(message: Message):
    await message.reply("My Commands: \n /start \n /info \n /code new \n")

@dp.message(Command("name"))
async def cmd_name(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        await message.answer(f"Hello, <b>{args[1]}</b>", parse_mode="HTML")
    else:
        await message.answer("Pls write your name after command /name")


@dp.message(Command("arbuz"))
async def cmd_name(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        await message.answer(f"selling for a one price, <b>{args[1]}</b>", parse_mode="HTML")
    else:
        await message.answer("Pls write /arbuz and number")


@dp.message(Command("code"))
async def cmd_name(message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) > 1:
        await message.answer(f"Error404.This unknown comma  <b>{args[1]}</b>", parse_mode="HTML")
    else:
        await message.answer(" write something after command /code")

@dp.message(Command("test"))
async def any_massage(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, <b>world</b>!", parse_mode="MarkdownV2")

@dp.message(Command("contact"))
async def cmd_name(message: Message):
    await message.reply("My contact: \n abs@dadas.org \n @TehpodershkaZero \n +88815659425489 \n")

@dp.message(Command("protocol"))
async def cmd_name(message: Message):
    await message.reply("Protocol: \n 72.215.100.250 \n 194.135.4.238 \n 180.3.12.124 \n 229.202.169.38 \n 36.87.202.235 \n")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

