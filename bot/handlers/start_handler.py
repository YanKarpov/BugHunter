from aiogram import types, Router
from aiogram.filters import Command

router = Router()

def register_start_handler(dp: Router):
    @router.message(Command('start'))
    async def start_command(message: types.Message):
        await message.reply("Я – BugHunter, помощник в сборе багов. Сообщи о проблеме и я передам ее нашим тестировщикам!")
    
    dp.include_router(router)
