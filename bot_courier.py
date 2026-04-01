"""Бот анонимный отправитель"""
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN_COURIER = "8748877093:AAFXVryNKYhU3CnmXyUDGuI5bnU8H68sjmM"  # ← Замените на свежий!

bot = Bot(token=TOKEN_COURIER)
dp = Dispatcher()

# Команда для анонимной отправки
@dp.message(Command("send"))
async def send_anonymous(msg: types.Message):
    """Анонимная отправка сообщения: /send <user_id> <text>"""
    user_id = msg.from_user.id
    print(f"📤 Пользователь {user_id} пытается отправить анонимное сообщение")
    
    # Парсим команду
    parts = msg.text.split(maxsplit=2)
    if len(parts) < 3:
        await msg.answer("❌ Формат: /send <user_id> <text>\nПример: /send 123456789 Привет!")
        return
    
    target_id = parts[1]
    text = parts[2]
    
    try:
        target_id = int(target_id)
    except ValueError:
        await msg.answer("❌ user_id должен быть числом!")
        return
    
    try:
        await bot.send_message(
            chat_id=target_id,
            text=text,
            parse_mode="Markdown"
        )
        await msg.answer(f"✅ Анонимное сообщение отправлено пользователю {target_id}")
        print(f"✅ Анонимное сообщение отправлено {target_id} от {user_id}")
    except Exception as e:
        await msg.answer(f"❌ Ошибка отправки: {e}")
        print(f"❌ Ошибка отправки анонимного сообщения {target_id}: {e}")

@dp.message(Command("start"))
async def start_handler(msg: types.Message):
    """Старт"""
    user_id = msg.from_user.id
    print(f"📩 /start от user_id={user_id}")
    await msg.answer(
        "🤫 **Анонимный отправитель**\n\n"
        "Отправляй сообщения анонимно:\n"
        "`/send <user_id> <text>`\n\n"
        "Пример: `/send 123456789 Привет, это анонимно!`\n\n"
        "Получатель увидит сообщение от этого бота.",
        parse_mode="Markdown"
    )

async def main():
    """Запуск бота"""
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())