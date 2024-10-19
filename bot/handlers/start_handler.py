from aiogram import types, Router, Bot
from aiogram.filters import Command


router = Router()

def register_start_handler(dp: Router, bot: Bot):
    @router.message(Command('start'))
    async def start_command(message: types.Message):
        await message.reply("Привет! Как я могу помочь?")

    dp.include_router(router)

