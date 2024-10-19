from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.db import save_bug_report  

router = Router()

class Form(StatesGroup):
    waiting_for_description = State()

category_mapping = {
    "category_not_opening": (1, "Не открывается"),
    "category_not_working": (2, "Работает некорректно"),
    "category_broken_layout": (3, "Сломалась верстка"),
    "category_vulnerability": (4, "Возможно, уязвимость"),
}

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

@router.callback_query()
async def process_category_selection(callback: types.CallbackQuery, state: FSMContext):
    selected_category = category_mapping.get(callback.data)
    if selected_category:
        category_id, category_name = selected_category
        await callback.answer()
        await callback.message.reply(
            f"Ты выбрал категорию <<{category_name}>>.\nТеперь опиши проблему (если ошибся с категорией, можешь вернуться к меню командой /report)."
        )
        await state.update_data(selected_category=category_id) 
        await state.set_state(Form.waiting_for_description)

@router.message(Command('report'))
async def report_command(message: types.Message, state: FSMContext):
    await state.finish()  
    await start_command(message) 

@router.message()
async def process_description(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    
    if current_state == Form.waiting_for_description.state:
        description = message.text
        data = await state.get_data()
        selected_category_id = data.get('selected_category')
        
        if selected_category_id and description:
            await save_bug_report(selected_category_id, description)
            await message.reply("Спасибо! Ваш отчет о проблеме успешно отправлен.")
            await state.finish() 
        else:
            await message.reply("Произошла ошибка. Пожалуйста, попробуйте снова.")



