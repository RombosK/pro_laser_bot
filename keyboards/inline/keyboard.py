from aiogram import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_COMMANDS_RU

dp: Dispatcher = Dispatcher()


# Функция генерации инлайн-клавиатуры автоматически в зависимости от ЛЕКСИКОНА
def create_inline_kb(width: int, *args: str, last_btn: str | None = None, last_btn1: str | None = None,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализация билдера
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализация списка кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполнение списка кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON_COMMANDS_RU[button] if button in LEXICON_COMMANDS_RU else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            if button == '/3':
                buttons.append(InlineKeyboardButton(text=text, url='https://t.me/OlgaKop77'))
            else:
                buttons.append(InlineKeyboardButton(text=text, callback_data=button))

    # Распаковка списка с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    if last_btn:
        kb_builder.row(InlineKeyboardButton(text=last_btn, url='https://t.me/OlgaKop77'))
    if last_btn1:
        kb_builder.row(InlineKeyboardButton(text=last_btn1, callback_data='last_btn1'))

    # Возврат объекта инлайн-клавиатуры
    return kb_builder.as_markup()

