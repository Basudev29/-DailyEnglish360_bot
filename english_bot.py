import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7881284043:AAH-RPn453KlOWTzWRPLObr3CtzDB6xBWxo"  # <-- Apna token yahan daalein
CHANNEL_USERNAME = "@DailyEnglish360"  # <-- Aapke channel ka username

lesson_text = """
🗣️ Aaj ka English Lesson:

🟢 Present Simple Tense:

Use for daily habits & facts.

🔸 I go to school.
🔸 She drinks tea.

✅ Roz practice kijiye. Fluency aayegi!
"""

# /start command response
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome! 🤖 Main aapka Spoken English Bot hoon. Roz English seekhne ke liye channel join kijiye : @DailyEnglish360"
    )

# Roz ka lesson bhejne wala function
async def send_daily_lesson(context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=CHANNEL_USERNAME, text=lesson_text)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # /start command handler
    app.add_handler(CommandHandler("start", start))

    # Daily job queue – subah 9 baje
    job_queue = app.job_queue
    job_queue.run_daily(send_daily_lesson, time=datetime.time(hour=9, minute=0, second=0))

    # Start polling
    app.run_polling()

if __name__ == "__main__":
    main()
