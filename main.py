import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update, context): await update.message.reply_text("Привет! Добро пожаловать в MIVO!")

app = Application.builder().token(os.environ["BOT_TOKEN"]).build()
app.add_handler(CommandHandler("start", start))
print("MIVO запущен...")
app.run_polling()