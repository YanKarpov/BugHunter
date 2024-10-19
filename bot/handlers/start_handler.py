from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router = Router()

def register_start_handler(dp: Router):
    @router.message(Command('start'))
    async def start_command(message: types.Message):
        welcome_text = (
            "Я – BugHunter, помощник в сборе багов. Сообщи о проблеме и я передам ее "
            "нашим тестировщикам!\n"
            "Чтобы начать, выбери категорию:"
        )
        
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Не открывается", callback_data="category_not_opening"),
                InlineKeyboardButton(text="Работает некорректно", callback_data="category_not_working"),
            ],
            [
                InlineKeyboardButton(text="Сломалась верстка", callback_data="category_broken_layout"),
                InlineKeyboardButton(text="Возможно, уязвимость", callback_data="category_vulnerability"),
            ],
        ])
        
        await message.reply(welcome_text, reply_markup=keyboard)
    
    dp.include_router(router)