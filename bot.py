import telebot
from telebot import types

TOKEN = "8540400273:AAEmdh9shyjdag1IUFgc8B0bI2qUTQYiyPs"

bot = telebot.TeleBot(TOKEN)

# 31 ta mavzu
topics = [
    "Cendlar",
    "AFU, SFU, FU, SELF FU, Inside FU",
    "Negationlar",
    "X2 va X3 Negation",
    "First, Third",
    "Likvidlik",
    "Major Minor Doji",
    "Doji",
    "LAL",
    "Imbalans",
    "Inside FU",
    "Self FU",
    "HCS modeli",
    "HCS X1, X2, X3",
    "HCS Negation",
    "HCS + Negation modeli",
    "True Stop Loss",
    "True Stop Loss bilan ishlash",
    "Time Frame Stretch",
    "TFS Established, Fresh, Closed",
    "Self Negation",
    "Entry modellari",
    "Special Candle",
    "0.1 Apart",
    "LAOL Negation",
    "X3 Negation",
    "X2 Manipulation",
    "X3 Manipulation",
    "X2 Negation",
    "True HCS",
    "Yo'nalish topish"
]


# =========================
# START
# =========================
@bot.message_handler(commands=["start"])
def start(message):

    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True
    )

    keyboard.row(
        "🎓 Discord Live",
        "ℹ️ Ma'lumot"
    )

    keyboard.row(
        "📚 Kurs haqida ma'lumot olish",
        "👤 Admin bilan bog'lanish"
    )

    bot.send_message(
        message.chat.id,
        "Assalomu alaykum! 👋\n\n"
        "🎓 <b>To'liq Bank Sistema</b> kursiga xush kelibsiz.\n\n"
        "Kerakli bo'limni tanlang.",
        parse_mode="HTML",
        reply_markup=keyboard
    )


# =========================
# DISCORD LIVE
# =========================
@bot.message_handler(
    func=lambda message: message.text == "🎓 Discord Live"
)
def discord_live(message):

    text = "🎓 <b>DISCORD LIVE</b>\n\n"
    text += "📚 <b>TO'LIQ BANK SISTEMA</b>\n\n"
    text += "Kursda quyidagi mavzular mavjud:\n\n"

    for i, topic in enumerate(topics, 1):
        text += f"{i}. {topic}\n"

    text += (
        "\n\n📌 Kurs haqida batafsil ma'lumot olish "
        "uchun administrator bilan bog'laning."
    )

    bot.send_message(
        message.chat.id,
        text,
        parse_mode="HTML"
    )


# =========================
# MA'LUMOT
# =========================
@bot.message_handler(
    func=lambda message: message.text == "ℹ️ Ma'lumot"
)
def information(message):

    bot.send_message(
        message.chat.id,
        "ℹ️ <b>MA'LUMOT</b>\n\n"
        "🎓 To'liq Bank Sistema — trading bo'yicha "
        "31 ta mavzuni o'z ichiga olgan kurs.\n\n"
        "Kursga ulanish va batafsil ma'lumot uchun "
        "administrator bilan bog'laning.",
        parse_mode="HTML"
    )


# =========================
# KURS HAQIDA
# =========================
@bot.message_handler(
    func=lambda message:
    message.text == "📚 Kurs haqida ma'lumot olish"
)
def course_info(message):

    bot.send_message(
        message.chat.id,
        "📚 <b>KURS HAQIDA</b>\n\n"
        "🎓 <b>To'liq Bank Sistema</b>\n\n"
        "📖 Kursda 31 ta mavzu mavjud.\n\n"
        "💵 <b>Narxi: $500</b>\n\n"
        "Kursga ulanish uchun administrator bilan "
        "bog'laning:\n\n"
        "👤 @laa_admin",
        parse_mode="HTML"
    )


# =========================
# ADMIN
# =========================
@bot.message_handler(
    func=lambda message:
    message.text == "👤 Admin bilan bog'lanish"
)
def admin(message):

    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
        types.InlineKeyboardButton(
            "💬 @laa_admin",
            url="https://t.me/laa_admin"
        )
    )

    bot.send_message(
        message.chat.id,
        "👤 <b>ADMIN BILAN BOG'LANISH</b>\n\n"
        "Kurs bo'yicha batafsil ma'lumot, "
        "to'lov va ulanish masalalari uchun "
        "administratorga yozing.",
        parse_mode="HTML",
        reply_markup=keyboard
    )


# =========================
# ISHGA TUSHIRISH
# =========================
print("✅ Bot ishlayapti...")

bot.infinity_polling(skip_pending=True)
