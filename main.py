import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Replace 'TELEGRAM_BOT_TOKEN' with the token you received from BotFather
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Главное меню
def main_menu():
    """Главное меню"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="😂 Смешные факты", callback_data="funny")],
        [InlineKeyboardButton(text="🎭 Шутки про Олега", callback_data="jokes")],
        [InlineKeyboardButton(text="💖 Милые секреты", callback_data="sweet")],
        [InlineKeyboardButton(text="😱 Шокирующие факты", callback_data="shocking")],
        [InlineKeyboardButton(text="🤫 То, что он скрывает", callback_data="reveal")]
    ])

# Старт
@dp.message(CommandStart())
async def start(msg: types.Message):
    """Старт"""
    args = msg.text.split(maxsplit=1)[1] if msg.text and ' ' in msg.text else None
    
    if args == "from_anon":
        await msg.answer(
            "🎭 **Досье загружено...**\n\n"
            "✅ Имя супруга: подтверждено (Олег)\n"
            "✅ Статус: \"Твой\" ❤️\n"
            "✅ Уровень секретности: 🔴 Высокий\n\n"
            "Выбери, что хочешь узнать:",
            reply_markup=main_menu(),
            parse_mode="Markdown"
        )
    else:
        await msg.answer("🔐 Доступ только по специальной ссылке.")

# Кнопки
@dp.callback_query(F.data == "funny")
async def funny_fact(call: types.CallbackQuery):
    """Смешные факты"""
    user_id = call.from_user.id
    print(f"😄 Пользователь {user_id} нажал 'Смешные факты'")
    await call.message.answer(
        "📊 **Факт #1:**\n"
        "Олег врет, что «не голоден», чтобы отдать тебе последний кусочек 🍕\n\n"
        "📊 **Факт #2:**\n"
        "Олег на 87% состоит из шуток, которые смешны только ему 😄\n\n"
        "📊 **Факт #3:**\n"
        "Он танцует под душем, представляя себя звездой рок-концерта 🎸\n\n"
        "[Ещё смешных фактов] | [➡️ Далее]",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Ещё смешных фактов", callback_data="more_funny")],
            [InlineKeyboardButton(text="➡️ Далее", callback_data="jokes")]
        ]),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "more_funny")
async def more_funny_fact(call: types.CallbackQuery):
    """Ещё смешные факты"""
    user_id = call.from_user.id
    print(f"😄 Пользователь {user_id} нажал 'Ещё смешных фактов'")
    await call.message.answer(
        "📊 **Факт #4:**\n"
        "Олег разговаривает с растениями, убеждая их расти быстрее 🌱\n\n"
        "📊 **Факт #5:**\n"
        "Он коллекционирует носки с супергероями, но носит только парные 🦸‍♂️\n\n"
        "📊 **Факт #6:**\n"
        "В детстве Олег мечтал стать супергероем, но стал программистом — почти то же самое 💻\n\n"
        "[➡️ Далее]",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="➡️ Далее", callback_data="jokes")
        ]]),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "jokes")
async def jokes_about_oleg(call: types.CallbackQuery):
    """Шутки про Олега"""
    user_id = call.from_user.id
    print(f"🎭 Пользователь {user_id} нажал 'Шутки про Олега'")
    await call.message.answer(
        "🎭 **Шутка #1:**\n"
        "Почему Олег всегда носит часы? Потому что время — деньги, а деньги — это код! ⌚💰\n\n"
        "🎭 **Шутка #2:**\n"
        "Олег говорит: 'Я не лентяй, я в режиме энергосбережения!' 🔋😴\n\n"
        "🎭 **Шутка #3:**\n"
        "Если Олег исчезнет, проверьте под столом — он, наверное, отлаживает код 🐛\n\n"
        "[Ещё шуток] | [➡️ Далее]",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Ещё шуток", callback_data="more_jokes")],
            [InlineKeyboardButton(text="➡️ Далее", callback_data="sweet")]
        ]),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "more_jokes")
async def more_jokes_about_oleg(call: types.CallbackQuery):
    """Ещё шуток про Олега"""
    user_id = call.from_user.id
    print(f"🎭 Пользователь {user_id} нажал 'Ещё шуток'")
    await call.message.answer(
        "🎭 **Шутка #4:**\n"
        "Олег: 'Я не спорю, я просто объясняю, почему ты не прав!' 🤓\n\n"
        "🎭 **Шутка #5:**\n"
        "Почему Олег любит чай? Потому что кофе — это Java, а чай — Python! ☕🐍\n\n"
        "[➡️ Далее]",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="➡️ Далее", callback_data="sweet")
        ]]),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "sweet")
async def sweet_secret(call: types.CallbackQuery):
    """Милые секреты"""
    user_id = call.from_user.id
    print(f"💖 Пользователь {user_id} нажал 'Милые секреты'")
    await call.message.answer(
        "💌 **Секрет #1:**\n"
        "Он смотрит на тебя, когда ты не видишь.\n"
        "Говорит, что ты «красивее всех» 🌹\n\n"
        "💌 **Секрет #2:**\n"
        "Он сохраняет ваши фото в отдельной папке «Моё счастье» 📸\n\n"
        "💌 **Секрет #3:**\n"
        "Каждый вечер перед сном он вспоминает ваш первый поцелуй 😘\n\n"
        "[Ещё секретов] | [➡️ Далее]",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Ещё секретов", callback_data="more_sweet")],
            [InlineKeyboardButton(text="➡️ Далее", callback_data="shocking")]
        ]),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "more_sweet")
async def more_sweet_secret(call: types.CallbackQuery):
    """Ещё милые секреты"""
    user_id = call.from_user.id
    print(f"💖 Пользователь {user_id} нажал 'Ещё секретов'")
    await call.message.answer(
        "💌 **Секрет #4:**\n"
        "Он пишет тебе сообщения даже когда ты рядом, просто чтобы сказать 'люблю' ❤️\n\n"
        "💌 **Секрет #5:**\n"
        "Твоя улыбка — его любимый вид спорта 🏆\n\n"
        "[➡️ Далее]",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="➡️ Далее", callback_data="shocking")
        ]]),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "shocking")
async def shocking_facts(call: types.CallbackQuery):
    """Шокирующие факты"""
    user_id = call.from_user.id
    print(f"😱 Пользователь {user_id} нажал 'Шокирующие факты'")
    await call.message.answer(
        "😱 **Шокирующий факт #1:**\n"
        "Олег однажды выиграл конкурс по поеданию пиццы... против холодильника! 🍕❄️\n\n"
        "😱 **Шокирующий факт #2:**\n"
        "Он знает все слова песни 'Never Gonna Give You Up', но никогда не признается 🎵\n\n"
        "😱 **Шокирующий факт #3:**\n"
        "Олег тайно тренируется быть супергероем — его суперсила: бесконечное терпение к багам 🦸‍♂️🐛\n\n"
        "[Ещё шокирующих фактов] | [➡️ Далее]",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Ещё шокирующих фактов", callback_data="more_shocking")],
            [InlineKeyboardButton(text="➡️ Далее", callback_data="reveal")]
        ]),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "more_shocking")
async def more_shocking_facts(call: types.CallbackQuery):
    """Ещё шокирующие факты"""
    user_id = call.from_user.id
    print(f"😱 Пользователь {user_id} нажал 'Ещё шокирующих фактов'")
    await call.message.answer(
        "😱 **Шокирующий факт #4:**\n"
        "Олег может программировать с закрытыми глазами... но предпочитает с открытыми, чтобы видеть ошибки 💻👀\n\n"
        "😱 **Шокирующий факт #5:**\n"
        "Он однажды пытался научить кота программировать — кот отказался, сказав 'мяу' вместо 'hello world' 🐱💻\n\n"
        "[➡️ Далее]",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="➡️ Далее", callback_data="reveal")
        ]]),
        parse_mode="Markdown"
    )

@dp.callback_query(F.data == "reveal")
async def final_reveal(call: types.CallbackQuery):
    """То, что он скрывает"""
    user_id = call.from_user.id
    print(f"🤫 Пользователь {user_id} нажал 'То, что он скрывает' — ПРАНК РАСКРЫТ! 🎉")
    await call.message.answer(
        "🎉 **ВНИМАНИЕ! ЭТО БЫЛ ЭКСПЕРИМЕНТ!** 🎉\n\n"
        "Все данные сгенерированы алгоритмом «Любовь-3000» специально для 1 апреля.\n\n"
        "Но одно утверждение — 100% правда:\n"
        "✨ Ты — лучшее, что случилось с Олегом. ✨\n\n"
        "**С 1 АПРЕЛЯ, никому не веря!** 🥳\n"
        "А теперь иди и обними своего «подопытного» 😄❤️"
    )

@dp.callback_query(F.data == "back")
async def back_menu(call: types.CallbackQuery):
    """Назад"""
    user_id = call.from_user.id
    print(f"🔙 Пользователь {user_id} вернулся в меню")
    await call.message.answer(
        "Выбери, что хочешь узнать:",
        reply_markup=main_menu()
    )

async def main():
    """Запуск бота"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())