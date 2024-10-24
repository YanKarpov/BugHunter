import os
import asyncio
from fastapi import FastAPI
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv
from handlers import send_welcome_message, handle_region_selection, handle_area_selection

load_dotenv()

app = FastAPI()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    raise ValueError("А токен где?")

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

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
async def region_selection(callback: types.CallbackQuery):
    await handle_region_selection(callback)

@dp.callback_query(lambda c: c.data.startswith("area_"))
async def area_selection(callback: types.CallbackQuery):
    await handle_area_selection(callback)

