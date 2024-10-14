from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""
Модуль с клавиатурами для взаимодействия с пользователем.

Описание:
- markup: Инлайн-клавиатура с двумя кнопками: "Узнать погоду" и "Есть вопросы".
"""

markup = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Узнать погоду ⛅️',
            callback_data='weather'
        )
    ],
    [
        InlineKeyboardButton(
            text='Есть вопросы 🆘',
            url='https://t.me/aleksgrekov',
            # callback_data='profile'
        )
    ]
])
