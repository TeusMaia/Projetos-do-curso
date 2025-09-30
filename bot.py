from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# ⚠️ Substitua este token por um NOVO gerado no @BotFather
BOT_TOKEN = ""

# Função para o comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Olá! Eu sou o Th4us_bot. Como posso te ajudar mn?')

# Função que responde a mensagens de texto
async def replay_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    resposta = f"Você disse: {user_text}\nEu sou um bot simples, mas já estou funcionando."
    await update.message.reply_text(resposta)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, replay_text))

    print("🤖 Bot iniciado... Pressione Ctrl+C para parar.")
    app.run_polling()

if __name__ == "__main__":
    main()
