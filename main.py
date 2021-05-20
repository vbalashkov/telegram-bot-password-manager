#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

from telebot import types

import buttons_configuration as btn_conf
import generate_password_chat
import request_password_chat
import delete_password_chat
from bot_module import bot


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am PasswordManagerBot.
I am here to make your passwords management easier! Let's start, to check all possible actions use /actions command\
""")


@bot.message_handler(commands=['actions'])
def suggest_possible_actions(message):
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(text='Create new password', callback_data=btn_conf.NEW_PASSWORD_CALLBACK_ID),
        types.InlineKeyboardButton(text='Request password', callback_data=btn_conf.REQUEST_PASSWORD_CALLBACK_ID),
        types.InlineKeyboardButton(text='Delete password', callback_data=btn_conf.DELETE_PASSWORD_CALLBACK_ID),
    )

    bot.send_message(message.from_user.id, text='Choose action you want', reply_markup=keyboard)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == btn_conf.NEW_PASSWORD_CALLBACK_ID:
        generate_password_chat.init(call)
    elif call.data == btn_conf.REQUEST_PASSWORD_CALLBACK_ID:
        request_password_chat.init(call)
    elif call.data == btn_conf.DELETE_PASSWORD_CALLBACK_ID:
        delete_password_chat.init(call)

bot.polling()
