from telegram import Bot
from datetime import date
import asyncio

nmt_bot = Bot("8593234150:AAGY-AxGhfdexphB6JBMo1K4bLqG2PqOyPY")
my_id = 1056631703
async def main():
    today = date.today()
    nmt = date(2026, 6, 1)
    day_left = (nmt - today).days

    if day_left > 0:
        await nmt_bot.sendMessage(chat_id= my_id,
                                  text=f"до нмт осталось {day_left} дней")
    elif day_left == 0:
        await nmt_bot.sendMessage(chat_id=my_id,
                                  text="Сегодня нмт")
    else:
        await nmt_bot.sendMessage(chat_id=my_id,
                                  text="Это мое последнее сообщение. Удачи с поступлением!")

asyncio.run(main())