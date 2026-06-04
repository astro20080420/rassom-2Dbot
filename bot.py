import os
import telebot
from fal_client import submit

# Tokenni Render'dagi Environment Variables'dan olamiz
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! 3D model uchun ta'rif yozing.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.reply_to(message, "Yaratilyapti, kuting...")
    try:
        # 3D model yaratish
        handler = submit("fal-ai/tripo-sr", arguments={"prompt": message.text})
        result = handler.get()
        bot.reply_to(message, f"Tayyor: {result['mesh_url']}")
    except Exception as e:
        bot.reply_to(message, f"Xatolik: {e}")

bot.polling() oling: {model_url}", chat_id=message.chat.id, message_id=msg.message_id)
    except Exception as e:
        bot.reply_to(message, f"Xatolik yuz berdi: {str(e)}")

# Botni ishga tushirish
if __name__ == "__main__":
    bot.infinity_polling()