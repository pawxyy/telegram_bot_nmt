from telegram import Bot
from datetime import date
import asyncio
import random

nmt_bot = Bot("8593234150:AAGY-AxGhfdexphB6JBMo1K4bLqG2PqOyPY")
admin_id = 1056631703


motivation_ru = ["Начинать всегда стоит с того, что сеет сомнения.",
                "Сложнее всего - начать.",
                "Маленькие шаги тоже движение вперед.",
                "Ошибки - часть пути.",
                "Ты сможешь! Верю в тебя. Люблю❤️"]

motivation_en = ["You should always start with what makes you doubt",
                "The hardest part is starting",
                "Small steps are always a way forward.",
                "Mistakes are part of the journey ",
                "You can do it! Im believe in you. Love u❤️️ "]
today_motivation_ru = motivation_ru[random.randint(0,4)]
today_motivation_en = motivation_en[random.randint(0,4)]



async def main():
    today = date.today()
    nmt = date(2026, 6, 1)
    day_left = (nmt - today).days

    if day_left > 0:
        await nmt_bot.sendMessage(chat_id= admin_id,
                                  text=f"До нмт осталось {day_left} дней")
        await asyncio.sleep(3600)

        await nmt_bot.sendMessage(chat_id=admin_id,
                                  text=f"{today_motivation_en}")
    elif day_left == 0:
        await nmt_bot.sendMessage(chat_id=admin_id,
                                  text="Сегодня нмт")
    else:
        await nmt_bot.sendMessage(chat_id=admin_id,
                                  text="Это мое последнее сообщение. Удачи с поступлением!")

asyncio.run(main())