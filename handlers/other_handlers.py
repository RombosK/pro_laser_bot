from aiogram import Router, types, Bot
from aiogram.types import FSInputFile, InputMediaPhoto
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Text
from config_bd import bd
from keyboards.inline.keyboard import create_inline_kb
from lexicon.lexicon import LEXICON_RU, LEXICON_COMMANDS_RU, LEXICON_COMMANDS_RU_TEST, LEXICON_SRC_HI_RU_TEST, \
    LEXICON_COMMANDS_RU_UPR, LEXICON_SRC_HI_RU_INFO

# Инициализируем роутер уровня модуля
router: Router = Router()
keyboard = create_inline_kb(2, **LEXICON_COMMANDS_RU)
keyboard_test = create_inline_kb(2, last_btn='Консультация 📞', last_btn1='Назад', **LEXICON_COMMANDS_RU_TEST)
keyboard_upr = create_inline_kb(2, last_btn='Консультация 📞', last_btn1='Назад', **LEXICON_COMMANDS_RU_UPR)
file = FSInputFile('start.jpg')
# file1 = FSInputFile('rf.jpg')
# file2 = FSInputFile('laser.jpg')
global m


async def glob(bot: Bot):
    await bot.delete_message(message_id=m.message_id, chat_id=m.chat.id)


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    global m
    m = await message.answer_photo(photo=file, caption=LEXICON_RU['/start'], reply_markup=keyboard)


# Обработчик нажатия на кнопку Назад
@router.callback_query(Text(text=['last_btn1']))
async def buttons_press_info(callback: CallbackQuery, bot: Bot):
    try:
        await glob(bot)
    except Exception:
        pass
    try:
        await callback.message.edit_media(
            media=InputMediaPhoto(media=file, caption=LEXICON_RU['/start']),
            reply_markup=keyboard
        )
    except Exception:
        global m
        m = await m.answer_photo(photo=file, caption=LEXICON_RU['/start'], reply_markup=keyboard)


# Обработчик нажатия на кнопку Лазерная эпиляция
@router.callback_query(Text(text=['/1']))
async def buttons_press_info(callback: CallbackQuery, bot: Bot):
    try:
        await glob(bot)
    except Exception:
        pass
    global m
    try:
        m = await m.answer(
            text='<b>Информация о лазерной эпиляции диодным лазером Lumenis</b>👇🏽',
            reply_markup=keyboard_upr
        )
    except Exception:
        m = await m.answer(
            text='<b>Информация о лазерной эпиляции диодным лазером Lumenis</b>👇🏽',
            reply_markup=keyboard_upr
        )


# Обработчик нажатия на кнопку RF-лифтинг
@router.callback_query(Text(text=['/2']))
async def buttons_press_rules(callback: CallbackQuery, bot: Bot):
    try:
        await glob(bot)
    except Exception:
        pass
    global m
    try:
        m = await m.answer(
            text='<b>Информация о процедуре RF-лифтинг</b>⬇️☺️',
            reply_markup=keyboard_test
        )

    except Exception:
        m = await m.answer(
            text='<b>Информация о процедуре RF-лифтинг</b>⬇️☺️',
            reply_markup=keyboard_test
        )


# Обработчик нажатия на кнопку Консультация
@router.callback_query(Text(text=['/3', 'last_btn']))
async def buttons_press_support(callback: CallbackQuery):
    await callback.answer(url='https://t.me/OlgaKop77')


# Обработчик нажатия на кнопку Описание
@router.callback_query(Text(text=['/1t']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.answer(
            text=LEXICON_SRC_HI_RU_TEST['/1t'],
            reply_markup=callback.message.reply_markup
        )
        # await callback.message.answer_photo(
        #     photo=file1, caption=LEXICON_SRC_HI_RU_TEST['/1t'],
        #     # media=InputMediaPhoto(media=file1, caption=LEXICON_SRC_HI_RU_TEST['/1t']),
        #     reply_markup=callback.message.reply_markup
        # )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_TEST['/1t'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку Стоимость
@router.callback_query(Text(text=['/2t']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.answer(
            text=LEXICON_SRC_HI_RU_TEST['/2t'],
            reply_markup=callback.message.reply_markup
        )
        # await callback.message.edit_media(
        #     media=InputMediaPhoto(media=file1, caption=LEXICON_SRC_HI_RU_TEST['/2t']),
        #     reply_markup=callback.message.reply_markup
        # )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_TEST['/2t'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку Противопоказания к процедуре
@router.callback_query(Text(text=['/3t']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.answer(
            text=LEXICON_SRC_HI_RU_TEST['/3t'],
            reply_markup=callback.message.reply_markup
        )
        # await callback.message.edit_media(
        #     media=InputMediaPhoto(media=file1, caption=LEXICON_SRC_HI_RU_TEST['/3t']),
        #     reply_markup=callback.message.reply_markup
        # )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_TEST['/3t'],
            reply_markup=callback.message.reply_markup
        )

# Обработчик нажатия на кнопку Коллаген
@router.callback_query(Text(text=['/4t']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.answer(
            text=LEXICON_SRC_HI_RU_TEST['/4t'],
            reply_markup=callback.message.reply_markup
        )

    except Exception:
        await callback.message.answer(
            text=LEXICON_SRC_HI_RU_TEST['/4t'],
            reply_markup=callback.message.reply_markup
        )

# Обработчик нажатия на кнопку Описание 
@router.callback_query(Text(text=['/1u']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.answer(
            text=LEXICON_SRC_HI_RU_INFO['/1u'],
            reply_markup=callback.message.reply_markup
        )
        # await callback.message.edit_media(
        #     media=InputMediaPhoto(media=file2, caption=LEXICON_SRC_HI_RU_INFO['/1u']),
        #     reply_markup=callback.message.reply_markup
        # )

    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_INFO['/1u'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку  Противопоказания 
@router.callback_query(Text(text=['/2u']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.answer(
            text=LEXICON_SRC_HI_RU_INFO['/2u'],
            reply_markup=callback.message.reply_markup
        )
        # await callback.message.edit_media(
        #     media=InputMediaPhoto(media=file2, caption=LEXICON_SRC_HI_RU_INFO['/2u']),
        #     reply_markup=callback.message.reply_markup
        # )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_INFO['/2u'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку   Как подготовиться 
@router.callback_query(Text(text=['/3u']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.answer(
            text=LEXICON_SRC_HI_RU_INFO['/3u'],
            reply_markup=callback.message.reply_markup
        )
        # await callback.message.edit_media(
        #     media=InputMediaPhoto(media=file2, caption=LEXICON_SRC_HI_RU_INFO['/3u']),
        #     reply_markup=callback.message.reply_markup
        # )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_INFO['/3u'],
            reply_markup=callback.message.reply_markup
        )


# Обработчик нажатия на кнопку  Преимущество 
@router.callback_query(Text(text=['/4u']))
async def buttons_press_info(callback: CallbackQuery):
    try:
        await callback.message.answer(
            text=LEXICON_SRC_HI_RU_INFO['/4u'],
            reply_markup=callback.message.reply_markup
        )
        # await callback.message.edit_media(
        #     media=InputMediaPhoto(media=file2, caption=LEXICON_SRC_HI_RU_INFO['/4u']),
        #     reply_markup=callback.message.reply_markup
        # )
    except Exception:
        await callback.message.edit_text(
            text=LEXICON_SRC_HI_RU_INFO['/4u'],
            reply_markup=callback.message.reply_markup
        )
