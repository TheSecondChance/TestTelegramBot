import telebot
from telebot import types
from telebot.types import WebAppInfo
import os



BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  button = types.KeyboardButton('See', web_app=WebAppInfo(url='https://hojigari.get-alpha.tech'))
  markup.add(button)
  bot.send_message(message.chat.id, "welcome to... ", reply_markup=markup)


 
@bot.message_handler(commands=["game"])
def send_game_message(message):
  markup = types.ReplyKeyboardMarkup(row_width=2)
  btn1 = types.KeyboardButton("/boo")
  btn2 = types.KeyboardButton("/help")
  btn3 = types.KeyboardButton("/close")
  markup.add(btn1, btn2, btn3)
  bot.send_message(chat_id=message.chat.id, text="what do you want",
                   reply_markup=markup)

@bot.message_handler(commands=["close"])
def send_game_message(message):
  markup = types.ReplyKeyboardRemove(selective=False)
  bot.send_message(chat_id=message.chat.id, text="see you agin",
                   reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text + " not correcte")
 
 

bot.infinity_polling()