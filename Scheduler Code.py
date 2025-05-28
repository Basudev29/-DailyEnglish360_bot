import asyncio
import datetime
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

TOKEN = "7881284043:AAH-RPn453KlOWTzWRPLObr3CtzDB6xBWxo"
CHANNEL_USERNAME = "@DailyEnglish360"

lesson_template = """
🗣️ *Daily English Lesson #{lesson_num}*

🎯 *Topic: {topic}*

🔟 *New Words:*
{words}

📘 *Story-Based Practice:*

{story}

💡 *Practice karo, fluency barhao!*

#SpokenEnglish #DailyEnglish #LearnEnglish
"""

# Example lessons list - aap isme apne lessons add kar sakte hain
lessons = [
    {
        "lesson_num": 1,
        "topic": "Self Introduction",
        "words": """1. Name – Naam
2. Age – Umar
3. Live – Rehna
4. City – Sheher
5. Student – Vidyarthi
6. Speak – Bolna
7. Learn – Seekhna
8. English – Angrezi
9. Hobby – Shauk
10. Friend – Dost""",
        "story": """🔹 A: Hello! My name is Ravi. (Namaste! Mera naam Ravi hai.)  
🔹 B: Hi Ravi! Where do you live? (Hi Ravi! Tum kahan rehte ho?)  
🔹 A: I live in Delhi. (Main Delhi mein rehta hoon.)  
🔹 B: Nice! I am a student. (Accha! Main ek vidyarthi hoon.)  
🔹 A: Me too! I am learning English. (Main bhi! Main angrezi seekh raha hoon.)"""
    },

    {
        "lesson_num": 2,
        "topic": "Daily Routine",
        "words": """1. Wake up – Jaagna
2. Brush – Brush karna
3. Eat – Khana
4. Work – Kaam
5. Study – Padhna
6. Sleep – Sona
7. Walk – Chalna
8. Run – Daudna
9. Clean – Saaf karna
10. Rest – Aaram karna""",
        "story": """🔹 A: What time do you wake up? (Tum kitne baje jaagte ho?)  
🔹 B: I wake up at 6 AM. (Main subah 6 baje jaagta hoon.)  
🔹 A: Do you brush your teeth? (Kya tum daant saaf karte ho?)  
🔹 B: Yes, every morning. (Haan, har subah.)  
🔹 A: Good! Then I eat breakfast. (Achha! Fir main nashta karta hoon.)"""
    },

    # Add more lessons here ...
]

async def send_daily_lesson(bot: Bot):
    # Calculate which lesson to send today based on date or other logic
    today = datetime.date.today()
    lesson_index = (today.toordinal() - lessons[0]['lesson_num']) % len(lessons)
    lesson = lessons[lesson_index]

    message = lesson_template.format(
        lesson_num=lesson['lesson_num'],
        topic=lesson['topic'],
        words=lesson['words'],
        story=lesson['story']
    )

    await bot.send_message(chat_id=CHANNEL_USERNAME, text=message, parse_mode="Markdown")

async def main():
    bot = Bot(token=TOKEN)
    scheduler = AsyncIOScheduler()
    
    # Schedule send_daily_lesson every day at 9:00 AM
    scheduler.add_job(lambda: asyncio.create_task(send_daily_lesson(bot)),
                      trigger="cron", hour=9, minute=0)
    
    scheduler.start()

    print("Bot started and scheduler is running. Press Ctrl+C to exit.")
    
    # Keep the program running
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
