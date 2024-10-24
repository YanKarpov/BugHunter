from aiogram import types

# Данные для категорий
categories = ["Категория 1", "Категория 2", "Категория 3"]

async def send_welcome_message(message: types.Message):
    welcome_text = (
        "Привет! Я бот, который готов помочь! Напишите название категории:\n"
        f"Доступные категории:\n" + "\n".join(categories)
    )
    await message.answer(welcome_text)

async def handle_category_selection(message: types.Message):
    selected_category = message.text

    # Проверка, является ли выбранная категория допустимой
    if selected_category in categories:
        await message.answer(f"Вы выбрали: {selected_category}. Чем я могу помочь?")
    else:
        await message.answer("Пожалуйста, выберите одну из категорий, написав ее название.")
