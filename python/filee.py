import asyncio
import logging

from aiogram import F, Bot, Dispatcher, types
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

@dp.message(Command("button"))
async def cmd_start(message: Message):
    kb = [
        [types.KeyboardButton(text="First button")],
        [types.KeyboardButton(text="Second button")]
        [types.KeyboardButton(text="Third button")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("What a button will you pick?", reply_markup=keyboard)

@dp.message(lambda message:message.text == "First button")
async def first_btn(message: Message):
    await message.reply("You press a first button")

@dp.message(lambda message:message.text == "Second button")
async def second_btn(message: Message):
    await message.reply("You press a second button")



@dp.message(Command("special_button"))
async def cmd_special_buttons(message: types.Message):
    kb=[
        [types.KeyboardButton(text="Request a contact", request_contact=True)],
        [types.KeyboardButton(text="Request a victorina", request_poll=types.KeyboardButtonPollType(type='quiz'))]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.reply("Select action" ,reply_markup=keyboard)



@dp.message(lambda message: message.text == "Send quiz")
async def send_quiz(message: types.Message):
    question = "What is a Japanese meal?"
    options = ["Taco", "Miso", "Pizza", "Doner"]

    correct_option_id = 1 

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        type="quiz",
        correct_option_id=correct_option_id,
        is_anonymous=False
    )

@dp.message(Command("extra"))
async def cmd_start(message: Message):
    kb = [
        [types.KeyboardButton(text="Send a ip")],
        [types.KeyboardButton(text="Link")],
        [types.KeyboardButton(text="Zero")],
        [types.KeyboardButton(text="Extra")],
        [types.KeyboardButton(text="Terminal")]
        
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("What a button will you pick?", reply_markup=keyboard)

@dp.message(lambda message:message.text == "Send a ip")
async def ip_btn(message: Message):
    await message.reply("Your IP:https://ipinfo.io/json")

@dp.message(lambda message:message.text == "Link")
async def link_bnt(message: Message):
    await message.reply("Link:https://youtu.be/ekY09M48Jvs?t=88")

@dp.message(lambda message: message.text == "Zero")
async def send_quiz(message: types.Message):
    question = "What is a Japanese meal?"
    options = ["Taco", "Miso", "Pizza", "Doner"]

    correct_option_id = 1 

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        type="quiz",
        correct_option_id=correct_option_id,
        is_anonymous=False
    )



@dp.message(lambda message:message.text == "Terminal")
async def terminal_btn(message: Message):
    await message.reply("Error 404 \n The button not finded \n")


@dp.message(F.content_type =="animation")
async def echo_gif(message:Message):
    await message.reply_animation(message.animation.file_id)




async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())

