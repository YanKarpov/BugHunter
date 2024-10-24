from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

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
    welcome_text = (
        "Привет! Это тестовое сообщение! Есть кнопки снизу?:\n"
    )
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=value, callback_data=key) for key, value in regions.items()]
    ])
    
    await message.answer(welcome_text, reply_markup=keyboard)

async def handle_region_selection(callback: types.CallbackQuery):
    selected_region = callback.data
    region_name = regions.get(selected_region, "Неизвестный район")

    await callback.answer()
    
    available_areas = areas.get(selected_region, [])
    
    if available_areas:
        area_keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=area, callback_data=f"area_{area}") for area in available_areas]
        ])
        await callback.message.answer(f"Вы выбрали: {region_name}. Выберите территорию:", reply_markup=area_keyboard)
    else:
        await callback.message.answer(f"Вы выбрали: {region_name}. У этого района нет территорий.")

async def handle_area_selection(callback: types.CallbackQuery):
    selected_area = callback.data.split("_", 1)[1]  
    await callback.answer()
    await callback.message.answer(f"Вы выбрали территорию: {selected_area}. Чем я могу помочь?")
