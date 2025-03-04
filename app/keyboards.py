from aiogram.types import (ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'),
                                      KeyboardButton(text='0 нас')]],
resize_keyboard=True,
input_field_placeholder='Выберите пункт меню...')

catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Фудболки', callback_data='t-shirt')],
    [InlineKeyboardButton(text='Крассовки', callback_data='sneakers')],
    [InlineKeyboardButton(text='Кепки', callback_data='cap')]])


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='отправить номер',
                                                           request_contact=True)]],
                                                           resize_keyboard=True)