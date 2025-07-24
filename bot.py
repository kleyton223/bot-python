print("Funcionando no Easypanel!")
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8102108405:AAFrFQ6vcZeQ0-S9rxZESBtgug9iNm9dvt0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Bot ativo e funcionando.")

async def ajuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Comandos disponíveis:\n/start - Iniciar bot\n/ajuda - Mostrar ajuda")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ajuda", ajuda))

    app.run_polling()

if __name__ == "__main__":
    main()
