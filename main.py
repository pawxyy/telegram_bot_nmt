import asyncio
from datetime import datetime, date, time
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from bot_token import BOT_TOKEN
import pytz

token = BOT_TOKEN
bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())

kyiv_time = pytz.timezone("Europe/Kyiv")
job_time = time(hour=10, minute=0, tzinfo=kyiv_time)

def day_word_uk(n):
    if 11 <= n % 100 <= 14:
        return "днів"
    elif n % 10 == 1:
        return "день"
    elif 2 <= n % 10 <= 4:
        return "дні"
    else:
        return "днів"

@dp.message(Command("start"))
async def start(message: Message):
    user_id = str(message.from_user.id)
    with open("user_id.txt", 'r') as f:
        content = f.read()
    if str(user_id) not in content:
        with open("user_id.txt", 'a') as f:
            f.write(f'{user_id}\n')
    await message.answer(f"Привіт, я твій бот до нмт! Коли ти складаєш нмт? Напиши це у форматі yyyy-mm-dd")

@dp.message(Command("change_date"))
async def change_date(message: Message):
    await message.answer(f"Добре! Напиши нову дату складання НМТ форматі yyyy-mm-dd")

def load_users():
    with open("user_id.txt", "r") as f:
        return [int(line.strip()) for line in f]

@dp.message(F.text)
async def count_day(message: Message):
    try:
        user_date = datetime.strptime(message.text, "%Y-%m-%d").date()
        today = date.today()
        days_left = (user_date - today).days

        if days_left > 0:
            await message.reply(f"До НМТ залишилось {days_left} {day_word_uk(days_left)}")
        elif days_left == 0:
            await message.reply(f"Сьогодні НМТ!! Бажаю іспіхів!!")
        else:
            await message.reply(f"Найскладніше вже позаду!! Я тебе вітаю!")

    except ValueError:
        await message.reply(f"Не той формат дати!! Спробуй yyyy-mm-dd")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())