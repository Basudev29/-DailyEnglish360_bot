import asyncio
from telegram import Bot
from telegram.ext import Application
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime

TOKEN = '7881284043:AAH-RPn453KlOWTzWRPLObr3CtzDB6xBWxo'
CHANNEL_USERNAME = '@DailyEnglish360'

# Sample daily lesson data (replace with your actual content source)
daily_words = [
    ["apple", "banana", "cat", "dog", "elephant", "fish", "goat", "hat", "ice", "jug"],
    ["kite", "lion", "monkey", "nose", "orange", "pen", "queen", "rat", "sun", "tree"],
    # Add more daily word lists here
]

daily_stories = [
    "Once upon a time, a little cat and dog became best friends.",
    "The lion and the monkey went on an adventure in the jungle.",
    # Add more stories here
]

lesson_index = 0

async def send_daily_lesson(bot: Bot):
    global lesson_index

    if lesson_index >= len(daily_words):
        lesson_index = 0  # Loop back to first lesson

    words = daily_words[lesson_index]
    story = daily_stories[lesson_index]

    lesson_text = "*Daily English Lesson*\n\n"
    lesson_text += "*10 New Words:*\n"
    lesson_text += ", ".join(words) + "\n\n"
    lesson_text += "*Story for Communication Practice:*\n"
    lesson_text += story

    await bot.send_message(chat_id=CHANNEL_USERNAME, text=lesson_text, parse_mode="Markdown")

    lesson_index += 1

async def main():
    bot = Bot(token=TOKEN)

    scheduler = AsyncIOScheduler()

    # Schedule daily lesson at 9:00 AM server time (change hour and minute as needed)
    scheduler.add_job(send_daily_lesson, "cron", hour=9, minute=0, args=[bot])

    scheduler.start()
    print(f"Scheduler started at {datetime.now()}")

    # Keep the program running.
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
