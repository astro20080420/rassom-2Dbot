import os
import telebot
from fal_client import submit

# Tokenni Render muhitidan olamiz (yoki shu yerga yangisini qo'yishingiz mumkin)
bot = telebot.TeleBot("7711125204:AAFc909wRK-SMlfAS-DH1nuswi9TsbSfJKE")

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! 3D model uchun ta'rif yozing.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        msg = bot.reply_to(message, "Kuting, 3D model yaratilyapti...")
        result = submit("fal-ai/tripo-sr", arguments={"prompt": message.text}).get()
        bot.edit_message_text(f"Tayyor: {result['mesh_url']}", message.chat.id, msg.message_id)
    except Exception as e:
        bot.reply_to(message, f"Xatolik: {e}")

bot.infinity_polling()
