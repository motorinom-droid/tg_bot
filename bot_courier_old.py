"""Бот анонимный отправитель"""
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN_COURIER = "8748877093:AAFXVryNKYhU3CnmXyUDGuI5bnU8H68sjmM"  # ← Замените на свежий!

bot = Bot(token=TOKEN_COURIER)
dp = Dispatcher()

# 🎣 Текст крючка
HOOK_TEXT = (
    "⚠️ **ВНИМАНИЕ!**\n\n"
    "**Вся правда о твоём муже!**\n\n"
    "Его ведь Олег зовут? 👀\n\n"
    "⏳ Сообщение удалится через 24 часа..."
)

# 🔗 Кнопка со ссылкой на второго бота
HOOK_KEYBOARD = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(
        text="🔗 Узнать, что он скрывает...",
        url="t.me/TruthAboutYourHusbandBot?start=from_anon"
    )
]])

async def send_hook():
    """Функция отправки крючка целевому пользователю"""
    print(f"🎣 Отправка крючка пользователю {TARGET_ID}...")
    try:
        await bot.send_message(
            chat_id=TARGET_ID,
            text=HOOK_TEXT,
            reply_markup=HOOK_KEYBOARD,
            parse_mode="Markdown"
        )
        print(f"✅ Крючок отправлен пользователю {TARGET_ID}")
    except Exception as e:
        print(f"❌ Ошибка отправки: {e}")
        print("💡 Возможные причины:")
        print("   1. Пользователь не нажимал /start в этом боте")
        print("   2. Неверный TARGET_ID")
        print("   3. Бот заблокирован пользователем")

@dp.message(CommandStart())
async def start_handler(msg: types.Message):
    """Обработчик /start - для первичной активации"""
    user_id = msg.from_user.id
    print(f"📩 /start от user_id={user_id}")

async def on_startup():
    """Выполняется при запуске бота"""
    print("🤖 Бот-курьер запущен...")
    # Небольшая задержка, чтобы бот успел подключиться к серверам Telegram
    await asyncio.sleep(2)
    await send_hook()

async def main():
    """Точка входа"""
    dp.startup.register(on_startup)  # Регистрируем хук на старт
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())