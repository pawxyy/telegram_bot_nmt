from telegram import Bot
from datetime import date
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import asyncio
import random
from bot_token import BOT_TOKEN

nmt_bot = Bot(BOT_TOKEN)
admin_id = 1056631703


motivation_uk = ["Починати завжди варто з того, що сіє сумніви.",
                "Найскладніше - почати.",
                "Маленькі кроки теж рух вперед.",
                "Помилки - частина шляху.",
                "Ти зможеш! Вірю в тебе. Люблю❤️"]

motivation_en = ["You should always start with what makes you doubt",
                "The hardest part is starting",
                "Small steps are always a way forward.",
                "Mistakes are part of the journey ",
                "You can do it! I believe in you. Love u❤️️ "]
today_motivation_uk = motivation_uk[random.randint(0,4)]
today_motivation_en = motivation_en[random.randint(0,4)]

async def start(update: Update, context: ContextTypes):
    user = update.effective_user
    lang = user.language_code
    today = date.today()
    nmt = date(2026, 6, 1)
    day_left = (nmt - today).days

    def day_word_uk(n):
        if 11 <= n % 100 <= 14:
            return "днів"
        elif n % 10 == 1:
            return "день"
        elif  2<= n % 10 <= 4:
            return "дні"
        else:
            return "днів"

    def day_word_en(n):
        if n > 1:
            return "days"
        else:
            return "day"

    if lang == "uk":
        if day_left > 0:
            await nmt_bot.sendMessage(chat_id= admin_id,
                                      text=f"До нмт лишилось {day_left} {day_word_uk(day_left)}")
            await asyncio.sleep(3600)

            await nmt_bot.sendMessage(chat_id=admin_id,
                                      text=f"{today_motivation_uk}")
        elif day_left == 0:
            await nmt_bot.sendMessage(chat_id=admin_id,
                                      text="Сьогодні НМТ, бажаю успіху! Ти складеш всі 4 предмети на 200!!")
        else:
            await nmt_bot.sendMessage(chat_id=admin_id,
                                      text="Це моє останнє повідомлення, бажаю успіхів зі вступом :D")
    elif lang == "en":
        if day_left > 0:
            await nmt_bot.sendMessage(chat_id= admin_id,
                                      text=f"{day_left} {day_word_en(day_left)} left until the NMT")
            await asyncio.sleep(3600)

            await nmt_bot.sendMessage(chat_id=admin_id,
                                      text=f"{today_motivation_en}")
        elif day_left == 0:
            await nmt_bot.sendMessage(chat_id=admin_id,
                                      text="Today is the NMT, good luck! You will get 200 on all 4 subjects!!")
        else:
            await nmt_bot.sendMessage(chat_id=admin_id,
                                      text="This is my last message, I wish you success with your admission :D")
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()