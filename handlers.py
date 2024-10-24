from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboard import create_region_keyboard, create_area_keyboard, create_feedback_keyboard

class FormStates(StatesGroup):
    waiting_for_area_selection = State()
    waiting_for_feedback = State()

regions = {
    "region_1": "Район 1",
    "region_2": "Район 2",
    "region_3": "Район 3",
    "region_4": "Район 4"
}

areas = { 
    "region_1": ["Территория А", "Территория Б"], 
    "region_2": ["Территория В", "Территория Г", "Территория Д"],
    "region_3": ["Территория Е", "Территория Ж", "Территория З"],
    "region_4": ["Территория И"]
}

async def send_welcome_message(message: types.Message):
    welcome_text = "Привет! Это тестовое сообщение! Есть кнопки снизу?:\n"
    keyboard = create_region_keyboard(regions)
    await message.answer(welcome_text, reply_markup=keyboard)

async def handle_region_selection(callback: types.CallbackQuery, state: FSMContext):
    selected_region = callback.data
    region_name = regions.get(selected_region, "Неизвестный район")

    await callback.answer()

    available_areas = areas.get(selected_region, [])

    if available_areas:
        area_keyboard = create_area_keyboard(available_areas)
        await callback.message.answer(f"Вы выбрали: {region_name}. Выберите территорию:", reply_markup=area_keyboard)
        await state.set_state(FormStates.waiting_for_area_selection)
    else:
        await callback.message.answer(f"Вы выбрали: {region_name}. У этого района нет территорий.")

async def handle_area_selection(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == "back_to_regions":
        await handle_back_to_regions(callback, state)  
    else:
        selected_area = callback.data.split("_", 1)[1]
        await callback.answer()
        await callback.message.answer(f"Вы выбрали территорию: {selected_area}. Чем я могу помочь?")
        await state.set_state(FormStates.waiting_for_feedback)

async def handle_back_to_regions(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await send_welcome_message(callback.message)  

async def handle_feedback(message: types.Message, state: FSMContext):
    if await state.get_state() == FormStates.waiting_for_feedback:
        user_feedback = message.text

        keyboard = create_feedback_keyboard()
        await message.answer(f"Спасибо за ваше предложение, передали в поддержку!", reply_markup=keyboard)
        await state.clear()