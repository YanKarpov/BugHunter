from aiogram import types, Router, Bot
from aiogram.filters import Command

router = Router()

def register_report_handler(dp: Router, bot: Bot):
    @router.message(Command('report'))
    async def report_command(message: types.Message):
        await message.reply("Пожалуйста, опишите проблему.")

    dp.include_router(router)


