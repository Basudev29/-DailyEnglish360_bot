import asyncio
from telegram import Bot

TOKEN = "7881284043:AAH-RPn453KlOWTzWRPLObr3CtzDB6xBWxo"
CHANNEL_USERNAME = "@DailyEnglish360"

lesson = """
🗣️ *Daily English Lesson #0 (Trial)*

🎯 *Topic: Self Introduction*

🔟 *New Words:*
1. Name – Naam
2. Age – Umar
3. Live – Rehna
4. City – Sheher
5. Student – Vidyarthi
6. Speak – Bolna
7. Learn – Seekhna
8. English – Angrezi
9. Hobby – Shauk
10. Friend – Dost

📘 *Story-Based Practice:*

🔹 A: Hello! My name is Ravi. (Namaste! Mera naam Ravi hai.)  
🔹 B: Hi Ravi! Where do you live? (Hi Ravi! Tum kahan rehte ho?)  
🔹 A: I live in Delhi. (Main Delhi mein rehta hoon.)  
🔹 B: Nice! I am a student. (Accha! Main ek vidyarthi hoon.)  
🔹 A: Me too! I am learning English. (Main bhi! Main angrezi seekh raha hoon.)

💡 *Practice karo, fluency barhao!*

#SpokenEnglish #DailyEnglish #LearnEnglish
"""

async def main():
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHANNEL_USERNAME, text=lesson, parse_mode="Markdown")

if __name__ == "__main__":
    asyncio.run(main())
