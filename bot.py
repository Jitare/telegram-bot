from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("🌙 Tu personaje despierta... ¿qué deseas explorar hoy?")

def chat(update, context):
    user_text = update.message.text
    response = f"Tu personaje responde: {user_text[::-1]}"  # Simulación
    update.message.reply_text(response)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

updater.start_polling()
updater.idle()
