import telebot
from telebot import types
import random
from datetime import datetime

TOKEN = "7963082537:AAFrVbaI7Dkpb61uz2i-91EkLh9ABIEfk3E"
bot = telebot.TeleBot(TOKEN)

USER_MOOD = {}  # {user_id: [{"value": 1..5, "ts": "..."}]}

AFFIRMATIONS = [
    "Я апну титана в доте",
    "Я достигну 10 лвл фэйсита",
    "Я пройду все соулслайки на платину",
    "Я пройду Малению с 1 трая",
]
TIPS = [
    "Relax бро",
    "Иди потрогай траву",
    "Разомни шею",
    "Иди попей а то че ты",
]

def main_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("Гидные медитации", "Дыхательные упражнения")
    kb.row("Майндсэт-трекер", "Советы по релаксации")
    kb.row("Ежедневные аффирмации")
    return kb

@bot.message_handler(commands=["start"])
def start(msg):
    bot.send_message(msg.chat.id, "Привет! Выбери функцию:", reply_markup=main_kb())

@bot.message_handler(func=lambda m: m.text == "Гидные медитации")
def guided_meditation(msg):
    text = (
        "Короткая медитация (2–3 мин):\n"
        "1) Сядьте удобно\n"
        "2) Вдох через нос на 4, выдох на 6\n"
        "3) Словите лютый вайб\n"
        "4) В конце глубоко вдохните и дальше по делам"
    )
    bot.send_message(msg.chat.id, text, reply_markup=main_kb())

@bot.message_handler(func=lambda m: m.text == "Дыхательные упражнения")
def breathing(msg):
    text = (
        "Дыхание:\n"
        "• 4-7-8: вдоооооооооооооох выыыыыыыыыыыыыыыыдох (4–5 циклов)\n"
        "• Квадрат: просто дыши, я в тебя верю (6 циклов)"
    )
    bot.send_message(msg.chat.id, text, reply_markup=main_kb())

@bot.message_handler(func=lambda m: m.text == "Майндсэт-трекер")
def mood_prompt(msg):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("1 💀", "2 🤦‍♂️", "3 🤷‍♂️", "4 🤪", "5 😈")
    kb.row("Назад")
    bot.send_message(msg.chat.id, "Оцените настроение от 1 до 5:", reply_markup=kb)

@bot.message_handler(func=lambda m: m.text in ["1 💀","2 🤦‍♂️","3 🤷‍♂️","4 🤪","5 😈"])
def mood_save(msg):
    uid = msg.from_user.id
    val = int(msg.text.split()[0])
    USER_MOOD.setdefault(uid, []).append({"value": val, "ts": datetime.now().isoformat()})
    bot.send_message(msg.chat.id, "Это топчик", reply_markup=main_kb())

@bot.message_handler(func=lambda m: m.text == "Советы по релаксации")
def tips(msg):
    picked = "\n".join(f"• {t}" for t in random.sample(TIPS, 3))
    bot.send_message(msg.chat.id, f"Советы по релаксации:\n\n{picked}", reply_markup=main_kb())

@bot.message_handler(func=lambda m: m.text == "Ежедневные аффирмации")
def affirmation(msg):
    bot.send_message(msg.chat.id, f"«{random.choice(AFFIRMATIONS)}»", reply_markup=main_kb())

@bot.message_handler(func=lambda m: m.text == "Назад")
def back(msg):
    bot.send_message(msg.chat.id, "Главное меню:", reply_markup=main_kb())

if __name__ == "__main__":
    print("Poshlo poehalo…")
    bot.polling(none_stop=True)