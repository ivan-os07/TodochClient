from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/registration")],
        [KeyboardButton(text="/help")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

help_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/registration")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)

register_kb = ...