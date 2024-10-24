import os
import asyncio
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from handlers import send_welcome_message, handle_region_selection, handle_area_selection, handle_feedback, handle_back_to_regions  # Добавьте сюда ваш обработчик для кнопки "Назад"

load_dotenv()

app = FastAPI()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    raise ValueError("А токен где?")

bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

@app.on_event("startup")
async def startup():
    await bot.delete_webhook(drop_pending_updates=True)
    asyncio.create_task(dp.start_polling(bot))

@app.get("/")
async def root():
    return {"message": "Ура, я работаю!!!"}

@dp.message(CommandStart())
async def start_command(message: types.Message):
    await send_welcome_message(message)

@dp.callback_query(lambda c: c.data.startswith("region_"))
async def region_selection(callback: types.CallbackQuery, state: FSMContext):
    await handle_region_selection(callback, state)

@dp.callback_query(lambda c: c.data.startswith("area_"))
async def area_selection(callback: types.CallbackQuery, state: FSMContext):
    await handle_area_selection(callback, state)

@dp.callback_query(lambda c: c.data == "back_to_regions")
async def back_to_regions(callback: types.CallbackQuery, state: FSMContext):
    await handle_back_to_regions(callback, state)  
@dp.message(lambda message: message.text.startswith("/"))
async def handle_c_message(message: types.Message):
    await message.answer("Команда не распознана. Попробуйте другую.")

@dp.message()
async def feedback_handler(message: types.Message, state: FSMContext):
    await handle_feedback(message, state)
