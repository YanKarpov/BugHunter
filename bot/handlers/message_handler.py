from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext  
from database.db import save_bug_report

async def send_welcome_message(message: types.Message):
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

async def handle_bug_report(description: str, selected_category_id: int, message: types.Message, state: FSMContext):
    if selected_category_id and description:
        await save_bug_report(selected_category_id, description)
        await message.reply("Спасибо! Ваш отчет о проблеме успешно отправлен.")
        await state.clear()  
    else:
        await message.reply("Произошла ошибка. Пожалуйста, попробуйте снова.")

