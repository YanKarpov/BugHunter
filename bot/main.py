import asyncio
from aiogram import Bot, Dispatcher
from bot.handlers.start_handler import register_start_handler
from bot.handlers.report_handler import register_report_handler
from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

register_start_handler(dp)
register_report_handler(dp)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())