import asyncio
from datetime import datetime, date, time
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot_token import BOT_TOKEN
import pytz

token = BOT_TOKEN
bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())

scheduler = AsyncIOScheduler(timezone="Europe/Kyiv")

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
    await message.answer(f"Привіт, я твій бот до нмт!<tg-emoji emoji-id='5458904472598095631'>👋</tg-emoji> \nКоли ти складаєш нмт? Напиши це у форматі yyyy-mm-dd ", parse_mode="HTML")

@dp.message(Command("change_date"))
async def change_date(message: Message):
    await message.answer(f"Добре! Напиши нову дату складання НМТ форматі yyyy-mm-dd <tg-emoji emoji-id='5449875850046481967'>🤔</tg-emoji>", parse_mode="HTML")

async def send_daily():
    with open("user_id.txt", 'r') as f:
        lines = f.readlines()
    today = date.today()
    for line in lines:
        user_id, user_date = line.strip().split(":")
        user_date = datetime.strptime(user_date, "%Y-%m-%d").date()
        days_left = (user_date - today).days
        if days_left > 0:
            await bot.send_message(chat_id=user_id, text = f"Нагадювання! До НМТ залишилось {days_left} {day_word_uk(days_left)}<tg-emoji emoji-id='5303081830738571591'>🤧</tg-emoji>", parse_mode="HTML")
        elif days_left == 0:
            await bot.send_message(chat_id=user_id, text = "Сьогодні НМТ!! Бажаю успіхів!!<tg-emoji emoji-id='5456149049214249060'>🥰</tg-emoji><tg-emoji emoji-id='5458696196749008675'>😍</tg-emoji>", parse_mode="HTML")


def load_users():
    with open("user_id.txt", "r") as f:
        return [int(line.strip()) for line in f]

@dp.message(F.text)
async def count_day(message: Message):
    try:
        user_date = datetime.strptime(message.text, "%Y-%m-%d").date()
        today = date.today()
        if user_date<today:
            await message.reply("Ця дата вже минула!<tg-emoji emoji-id='5334549028891796220'>😠</tg-emoji> Обери іншу", parse_mode="HTML")
        days_left = (user_date - today).days
        if days_left > 0:
                await message.reply(f"До НМТ залишилось {days_left} {day_word_uk(days_left)}<tg-emoji emoji-id='5303081830738571591'>🤧</tg-emoji>", parse_mode="HTML")
        elif days_left == 0:
            await message.reply(f"Сьогодні НМТ!! Бажаю успіхів!!<tg-emoji emoji-id='5456149049214249060'>🥰</tg-emoji><tg-emoji emoji-id='5458696196749008675'>😍</tg-emoji>", parse_mode="HTML")
    except ValueError:
        await message.reply(f"Не той формат дати!!<tg-emoji emoji-id='5226962730941955595'>🙄</tg-emoji> Спробуй yyyy-mm-dd", parse_mode="HTML")



    user_id = str(message.from_user.id)
    user_date_exam = f"{user_id}:{message.text}\n"
    try:
        with open("user_id.txt", 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    new_lines = []
    found = False
    for line in lines:
        if line.startswith(user_id + ":"):
            new_lines.append(user_date_exam)
            found = True
        else:
            new_lines.append(line)
    if not found:
        new_lines.append(user_date_exam)
    with open("user_id.txt", 'w') as f:
        f.writelines(new_lines)

async def main():
    scheduler.add_job(send_daily, "cron", hour=10, minute=20)
    scheduler.start()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())