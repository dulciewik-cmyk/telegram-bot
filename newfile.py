
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ضع التوكن الجديد من BotFather هنا
TOKEN = "9059941502:AAF5Spxk9-5o_hWw9zfaVAklEQY2g0aC6LE"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بيك ❤️\n"
        "أنا بوت بايثون شغال من Pydroid 3!\n"
        "ابعتلي أي رسالة وأنا هرد عليك."
    )


async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text

    await update.message.reply_text(
        f"وصلت رسالتك بنجاح ✅\n"
        f"أنت كتبت: {message}"
    )


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
    )

    print("BOT IS RUNNING...")

    app.run_polling()


if __name__ == "__main__":
    main()
