import asyncio
import os
import random
from aiogram import Bot, Dispatcher, F, types
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("Не найден TELEGRAM_BOT_TOKEN в .env")

bot = Bot(token=TOKEN)
dp = Dispatcher()


WRITERS = ["Хемингуэй", "Толстой", "Достоевский", "Чехов", "Булгаков"]
POETS = ["Шекспир", "Пушкин", "Есенин", "Ахматова", "Маяковский"]
BOOKS = ["Три товарища", "Война и мир", "Преступление и наказание", "Мастер и Маргарита", "1984"]
MONOLOGUES = [
    "Быть или не быть",
    "Что делать?",
    "А судьи кто?",
    "Человек — это звучит гордо",
    "Все счастливые семьи похожи друг на друга"
]

@dp.message(F.command() == "start")
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Напиши:\n"
        "«Писатель» — дам случайную фамилию писателя\n"
        "«Поэт» — случайную фамилию поэта\n"
        "«Книга» — случайное название книги\n"
        "«Монолог» — случайный известный монолог"
    )

@dp.message(F.text.lower() == "писатель")
async def handle_writer(message: types.Message):
   await message.answer(random.choice(WRITERS))

@dp.message(F.text.lower() == "поэт")
async def handle_poet(message: types.Message):
   await message.answer(random.choice(POETS))

@dp.message(F.text.lower() == "книга")
async def handle_book(message: types.Message):
    await message.answer(random.choice(BOOKS))

@dp.message(F.text.lower() == "монолог")
async def handle_monologue(message: types.Message):
   await message.answer(random.choice(MONOLOGUES))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
