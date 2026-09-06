from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

BOT_TOKEN = "8451192627:AAEieNo5a0cy8R1ZUFMlJmWydfModakoGvA"

async def start(update: Update, context):
    await update.message.reply_text('👋 Привет! Я фитнес-бот!')

async def echo(update: Update, context):
    await update.message.reply_text(f'Ты написал: {update.message.text}')

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("✅ Бот @TermuxFitnessBot запущен на телефоне!")
app.run_polling()
