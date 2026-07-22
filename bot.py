import telebot
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

print("TOKEN BOR:", bool(TOKEN))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Ishladim 🤖")

bot.infinity_polling()
