import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Menga musiqa havolasini yuboring.")

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("Yuklanmoqda...")
    ydl_opts = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'}], 'outtmpl': 'music.mp3'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl: ydl.download([url])
    await update.message.reply_audio(audio=open('music.mp3', 'rb'))
    os.remove('music.mp3')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), download))
    app.run_polling()

import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from flask import Flask
from threading import Thread

# Web server qismi (Render port so'ramasligi uchun)
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot ishlayapti!"

def run_web():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

# Bot qismi
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Menga musiqa havolasini yuboring.")

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("Yuklanmoqda...")
    # ... (oldingi yuklash kodi qoladi) ...

if __name__ == '__main__':
    # Web serverni fonda ishga tushirish
    Thread(target=run_web).start()
    
    # Botni ishga tushirish
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler('start', start))
    app_bot.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), download))
    app_bot.run_polling()
