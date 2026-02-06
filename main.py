from telegram import Bot
from datetime import date
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
                "You can do it! Im believe in you. Love u❤️️ "]
today_motivation_uk = motivation_uk[random.randint(0,4)]
today_motivation_en = motivation_en[random.randint(0,4)]

async def main():
    today = date.today()
    nmt = date(2026, 6, 1)
    day_left = (nmt - today).days

    def day_word(n):
        if 11 <= n % 100 <= 14:
            return "днів"
        elif n % 10 == 1:
            return "день"
        elif  2<= n % 10 <= 4:
            return "дні"
        else:
            return "днів"


    if day_left > 0:
        await nmt_bot.sendMessage(chat_id= admin_id,
                                  text=f"До нмт лишилось {day_left} {day_word(day_left)}")
        await asyncio.sleep(3600)

        await nmt_bot.sendMessage(chat_id=admin_id,
                                  text=f"{today_motivation_uk}")
    elif day_left == 0:
        await nmt_bot.sendMessage(chat_id=admin_id,
                                  text="Сьогодні НМТ, бажаю успіху! Ти складеш всі 4 предмети на 200!!")
    else:
        await nmt_bot.sendMessage(chat_id=admin_id,
                                  text="Це моє останнє повідомлення, бажаю успіхів зі вступом)")
asyncio.run(main())