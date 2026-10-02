import os
import telebot
from aiohttp import web

# 1. Token va Portni olish
BOT_TOKEN = os.environ.get("BOT_TOKEN")
PORT = int(os.environ.get("PORT", 10000))

if not BOT_TOKEN:
    raise ValueError("XATOLIK: BOT_TOKEN topilmadi!")

bot = telebot.TeleBot(BOT_TOKEN)

# 2. 31 ta mavzu ro'yxati
topics = [
    "Cendlar", "AFU, SFU, FU, SELF FU, Inside FU", "Negationlar", "X2 va X3 Negation",
    "First, Third", "Likvidlik", "Major Minor Doji", "Doji", "LAL", "Imbalans",
    "Inside FU", "Self FU", "HCS modeli", "HCS X1, X2, X3", "HCS Negation",
    "HCS + Negation modeli", "True Stop Loss", "True Stop Loss bilan ishlash",
    "Time Frame Stretch", "TFS Established, Fresh, Closed", "Self Negation",
    "Entry modellari", "Special Candle", "0.1 Apart", "LAOL Negation",
    "X3 Negation", "X2 Manipulation", "X3 Manipulation", "X2 Negation",
    "True HCS", "Yo'nalish topish"
]

# 3. Bot buyruqlari
@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("🎓 Discord Live", "ℹ️ Ma'lumot")
    keyboard.row("📚 Kurs haqida ma'lumot olish", "👤 Admin bilan bog'lanish")
    
    text = (
        "Assalomu alaykum! 👋\n\n"
        "🎓 <b>To'liq Bank Sistema</b> kursiga xush kelibsiz.\n\n"
        "Kerakli bo'limni tanlang."
    )
    bot.send_message(message.chat.id, text, parse_mode="HTML", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "🎓 Discord Live")
def discord_live(message):
    text = "🎓 <b>DISCORD LIVE</b>\n\n📚 <b>TO'LIQ BANK SISTEMA</b>\n\nKurs mavzulari:\n\n"
    for i, topic in enumerate(topics, 1):
        text += f"{i}. {topic}\n"
    bot.send_message(message.chat.id, text, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "ℹ️ Ma'lumot")
def information(message):
    text = "ℹ️ <b>MA'LUMOT</b>\n\n🎓 To'liq Bank Sistema — 31 ta mavzudan iborat kurs."
    bot.send_message(message.chat.id, text, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "📚 Kurs haqida ma'lumot olish")
def course_info(message):
    text = (
        "📚 <b>KURS HAQIDA</b>\n\n"
        "🎓 <b>To'liq Bank Sistema</b>\n\n"
        "📖 Mavzular: 31 ta\n\n"
        "💵 <b>Narxi: $500</b>\n\n"
        "Ulanish uchun: 👤 @laa_admin"
    )
    bot.send_message(message.chat.id, text, parse_mode="HTML")

@bot.message_handler(func=lambda message: message.text == "👤 Admin bilan bog'lanish")
def admin(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(telebot.types.InlineKeyboardButton("💬 @laa_admin", url="https://t.me/laa_admin"))
    bot.send_message(message.chat.id, "👤 Admin bilan bog'lanish uchun pastdagi tugmani bosing:", reply_markup=keyboard)

# 4. Aiohttp veb-serveri (Render port talabini qondirish uchun)
async def handle(request):
    return web.Response(text="Bot ishlayapti!")

app = web.Application()
app.router.add_get("/", handle)

async def main():
    # Veb-serverni sozlash
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"✅ Veb-server {PORT}-portda ishga tushdi!")

    # Botni ishga tushirish (polling)
    print("✅ Bot ishga tushmoqda...")
    await bot.infinity_polling(skip_pending=True)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
