# bot.py ning oxirgi qismi
if __name__ == '__main__':
    # Boshqa thread-larni o'chiring, faqat bitta "app" ishlasin
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), download))
    
    # Webhook orqali ishga tushirish (Polling o'rniga)
    PORT = int(os.environ.get("PORT", 10000))
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url="https://music-bot-4-bf49.onrender.com/" + TOKEN # O'z URL ingiz
    )

        # MP3 olish uchun eng optimal sozlamalar ydl_opts = {
            'format': 'bestaudio', 
            'outtmpl': 'music.mp3',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
