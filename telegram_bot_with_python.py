from telegram.ext import ApplicationBuilder, CommandHandler

async def hello(update, context):
    await update.message.reply_text("Hello, World 👋")

def main():
    app = ApplicationBuilder().token("Your Bot Token").build()
    app.add_handler(CommandHandler("hello", hello))

    print("🤖 Bot is running... Press Ctrl+C to stop")
    app.run_polling()

if __name__ == "__main__":
    main()
