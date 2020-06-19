import telebot
import random

from telebot.types import Message

TOKEN='1220314354:AAFdHnon2wR-9RDpV5xAYKnBlZ_gcgjjcHo'
bot = telebot.TeleBot(TOKEN)

smile= [
    '😂',
    '😘',
    '❤',
    '😍',
    '😊',
    '😁',
    '👍'
        ]

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message,'Привет')

@bot.message_handler(func=lambda message: True)
def upper(message: Message):
    bot.reply_to(message, random.choice(smile))



bot.polling()
