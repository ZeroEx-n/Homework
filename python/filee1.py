import asyncio
import logging
import random
import requests
import pyttsx3
import subprocess

from aiogram import F, Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup,ContentType 

#login
logging.basicConfig(level=logging.INFO)
bot = Bot(token='7759664843:AAGjRGBIIvwtD0CGkF1m-y-U5DWqjHKsbwE')
dp = Dispatcher()


#commands
@dp.message(Command("start"))
async def cmd_name(message: Message):
    user_id = message.from_user.id 
    logging.info(f"User ID:{user_id}has triggered the /start command" )
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

#buttons
@dp.message(lambda message:message.text == "First button")
async def first_btn(message: Message):
    await message.reply("You press a first button")

@dp.message(lambda message:message.text == "Second button")
async def second_btn(message: Message):
    await message.reply("You press a second button")


#commands for buttons
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
    question = "What is a Japanese meal😀?"
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

btn_keyboard= ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Horror")],
        [KeyboardButton(text="Action")],
        [KeyboardButton(text="Humor")],
        [KeyboardButton(text="Fantastic")],
         [KeyboardButton(text="Biographies")],
        [KeyboardButton(text="Psychological")],
        [KeyboardButton(text="Historical")],
        [KeyboardButton(text="Cartoons")],
        [KeyboardButton(text="Anime")]
    ],
    resize_keyboard=True
)

horror = ["https://www.kinopoisk.ru/film/5198/", "https://www.kinopoisk.ru/film/386/", "https://www.kinopoisk.ru/film/16015/", "https://www.kinopoisk.ru/film/251790/", "https://www.kinopoisk.ru/film/481932/"]
action = ["https://www.kinopoisk.ru/film/1008444/", "https://www.kinopoisk.ru/film/301/", "https://www.kinopoisk.ru/film/7410/", "https://www.kinopoisk.ru/film/471/", "https://www.kinopoisk.ru/film/332/"]
humor = ["https://www.kinopoisk.ru/film/5185/", "https://www.kinopoisk.ru/film/42782/", "https://www.kinopoisk.ru/film/8124/", "https://www.kinopoisk.ru/film/6039/", "https://www.kinopoisk.ru/film/42664/"]
fantastic = ["https://www.kinopoisk.ru/film/507/", "https://www.kinopoisk.ru/film/1199100/", "https://www.kinopoisk.ru/film/843649/", "https://www.kinopoisk.ru/film/301/", "https://www.kinopoisk.ru/film/258687/"]
biographies =["https://www.kinopoisk.ru/film/4664634/", "https://www.kinopoisk.ru/film/649917/", "https://www.kinopoisk.ru/film/803422/", "https://www.kinopoisk.ru/film/835086/", "https://www.kinopoisk.ru/film/1108577/"]
psychological = ["https://www.kinopoisk.ru/film/397667/", "https://www.kinopoisk.ru/film/530/", "https://www.kinopoisk.ru/film/447301/", "https://www.kinopoisk.ru/film/462606/" , "https://www.kinopoisk.ru/film/944098/"]
historical = ["https://www.kinopoisk.ru/film/474/", "https://www.kinopoisk.ru/film/1045893/", "https://www.kinopoisk.ru/film/5020767/", "https://www.kinopoisk.ru/film/1008113/", "https://www.kinopoisk.ru/film/5388914/"]
cartoons = ["https://www.kinopoisk.ru/film/775276/", "https://www.kinopoisk.ru/film/430/", "https://www.kinopoisk.ru/film/42326/", "https://www.kinopoisk.ru/series/584136/", "https://www.kinopoisk.ru/film/775273/"]
anime = ["https://www.kinopoisk.ru/series/749374/", "https://www.kinopoisk.ru/film/958722/", "https://www.kinopoisk.ru/series/1381125/", "https://www.kinopoisk.ru/series/707636/", "https://www.kinopoisk.ru/series/452973/"]
 
@dp.message(Command("films"))
async def cmd_name(message: Message):
    await message.answer("Choose a genre", reply_markup=btn_keyboard)

@dp.message(lambda message: message.text == "Horror")
async def show_horror(message: Message):
    await message.reply("Horror " + random.choice(horror))

@dp.message(lambda message: message.text == "Action")
async def show_action(message: Message):
    await message.reply("Action " + random.choice(action))

@dp.message(lambda message: message.text == "Humor")
async def show_humor(message: Message):
    await message.reply("Humor " + random.choice(humor))

@dp.message(lambda message: message.text == "Fantastic")
async def show_fantastic(message: Message):
    await message.reply("Fantastic " + random.choice(fantastic))

@dp.message(lambda message: message.text == "Biographies")
async def show_biographies(message: Message):
    await message.reply("Biographies " + random.choice(biographies))

@dp.message(lambda message: message.text == "Psychological")
async def show_psychological(message: Message):
    await message.reply("Psychological " + random.choice(psychological))

@dp.message(lambda message: message.text == "Historical")
async def show_gistorical(message: Message):
    await message.reply("Historical " + random.choice(historical))

@dp.message(lambda message: message.text == "Cartoons")
async def show_cartoons(message: Message):
    await message.reply("Cartoons " + random.choice(cartoons))

@dp.message(lambda message: message.text == "Anime")
async def show_anime(message: Message):
    await message.reply("Anime " + random.choice(anime))



@dp.message(lambda message:message.text == "Terminal")
async def terminal_btn(message: Message):
    await message.reply("Error 404 \n The button not finded \n")


@dp.message(F.content_type =="animation")
async def echo_gif(message:Message):
    await message.reply_animation(message.animation.file_id)

@dp.message(Command("spam"))
async def spam_btn(message: Message):
    for i in range(100, 1, -1):
        await message.reply(str(i))


@dp.message(Command("game"))
async def launch_game(message: Message):
    def run_game():
        try:
            subprocess.Popen("C:\ProgramFiles (x86)\Steam\steam.exe")
            return "Steam open"
        except FileNotFoundError:
            return "Way not founded. Check way"

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, run_game)

    await message.reply(response)

@dp.message(Command("google"))
async def launch_google(message: Message):
    def run_google():
        try:
            subprocess.Popen("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
            return "Google open"
        except FileNotFoundError:
            return "Way not founded. Check way"

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, run_google)

    await message.reply(response)


@dp.message(Command("discord"))
async def launch_telegram(message: Message):
    def run_discord():
        try:
            subprocess.Popen("C:\Program Files (x86)\Discord\Discord.exe")
            return "Discord open"
        except FileNotFoundError:
            return "Way not founded. Check way"

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, run_discord)

    await message.reply(response)


@dp.message(Command("telegram"))
async def launch_telegram(message: Message):
    def run_telegram():
        try:
            subprocess.Popen("C:\Program Files (x86)\Telegram\Telegram.exe")
            return "Telegram open"
        except FileNotFoundError:
            return "Way not founded. Check way"

    loop = asyncio.get_event_loop()
    response = await loop.run_in_executor(None, run_telegram)

    await message.reply(response)



@dp.message(Command("weather"))
async def start_command(message:types.Message):
    await message.answer("Select a city for weather")


@dp.message(F.text)
async def get_weather(message:types.Message):
    city = message.text
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347"
        weather_data = requests.get(url).json()

        temperature = weather_data["main"]["temp"]
        temperature_feels = weather_data["main"]["feels_like"]
        wind_speed = weather_data['wind']['speed']
        clouds_cover = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']

        await message.answer(f'Air temperature: {temperature}\n'
                             f'Feelins like: {temperature_feels}\n'
                             f'Wind: {wind_speed}\n'
                             f'Cloudy: {clouds_cover}\n'
                             f'Humidity:{humidity}%')
        pass
    except KeyError:
        await message.answer("Сould not determine the city")

# engine = pyttsx3.init()

# engine.setProperty("rate", 150)
# engine.setProperty("volume", 0.9)

# engine.say("?")

# engine.runAndWait()

async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
