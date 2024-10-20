import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.handlers.bug_handler import router as start_router  
from config import TELEGRAM_TOKEN

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

bot = Bot(token=TELEGRAM_TOKEN)
storage = MemoryStorage()  
dp = Dispatcher(storage=storage)

dp.include_router(start_router)

async def main():
    logger.info("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        logger.info("Запуск бота...")
        asyncio.run(main())
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}")