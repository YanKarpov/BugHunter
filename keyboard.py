from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from typing import List

# Кнопка для выбора района
def create_region_keyboard(regions: dict) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=value, callback_data=key)] for key, value in regions.items()
    ])

# Кнопки для выбора территории
def create_area_keyboard(available_areas: List[str]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=area, callback_data=f"area_{area}")] for area in available_areas
    ] + [[InlineKeyboardButton(text="Назад", callback_data="back_to_regions")]])

# Кнопкаа для дополнения сообщения
def create_feedback_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Дополнить сообщение", callback_data="back_to_regions")]
    ])
