#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import os
import dotenv
import telebot

dirpath = os.getcwd()
dotenv_file = os.path.join(dirpath, './.env')

if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

API_TOKEN = os.environ['SECRET_TELEGRAM_API_KEY']

bot = telebot.TeleBot(API_TOKEN)
