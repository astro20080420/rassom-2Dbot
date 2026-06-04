import os
import telebot
from fal_client import submit

TOKEN = "8744906457:AAHFvUOS4Fnfv8GmZAsCGXTwe9gp-BeQmpg"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! 3D model uchun so'z yozing.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    msg = bot.reply_to(message, "Kuting, 3D model yaratilyapti...")
    try:
        res = submit("fal-ai/tripo-sr", arguments={"prompt": message.text})
        data = res.get()
        bot.edit_message_text(f"Tayyor: {data['mesh_url']}", message.chat.id, msg.message_id)
    except Exception as e:
        bot.edit_message_text(f"Xatolik: {e}", message.chat.id, msg.message_id)

bot.polling(none_stop=True)
