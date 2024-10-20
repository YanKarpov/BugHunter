from aiogram import types, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from bot.handlers.message_handler import send_welcome_message, handle_bug_report

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
    await send_welcome_message(message)

@router.callback_query(lambda c: c.data == "new_problem")
async def process_new_problem(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await send_welcome_message(callback.message)
    await state.clear()
    
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
    await state.clear()
    await send_welcome_message(message)

@router.message()
async def process_description(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    
    if current_state == Form.waiting_for_description.state:
        description = message.text
        data = await state.get_data()
        selected_category_id = data.get('selected_category')
        
        await handle_bug_report(description, selected_category_id, message, state)