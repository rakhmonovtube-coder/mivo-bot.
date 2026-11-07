import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Добро пожаловать в MIVO!")

def main():
    app = Application.builder().token(os.environ["9175798250:AAGXS2yaPoi6WJrs-F5BmIQYjEFtXEyGFhU"]).build()
    app.add_handler(CommandHandler("start", start))
    print("MIVO запущен!")
    app.run_polling()

if name == "main":
    main()
