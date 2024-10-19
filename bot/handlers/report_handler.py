from aiogram import types, Router
from aiogram.filters import Command
from database.db import save_bug_report  

router = Router()

def register_report_handler(dp: Router):
    @router.message(Command('report'))
    async def report_command(message: types.Message):
        await message.reply("Пожалуйста, опишите проблему.")
        description = "Тестовое сообщение о проблеме."
        await save_bug_report(1, description)  
    
    dp.include_router(router)



