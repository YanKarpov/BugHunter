import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.handlers.start_handler import router as start_router  
from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()  
dp = Dispatcher(storage=storage)

dp.include_router(start_router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
