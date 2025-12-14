from aiogram import Bot, Dispatcher, executor, types

TOKEN = "8416735074:AAHyyD3PMVy7O9qRMeB4a4PLlSeE41Ff0hU"
ADMIN_ID = 8453542515

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "Если у вас есть интересное видео, фото, тик ток и прочее для стрима "
        "и вы хотите чтобы Вика это оценила, скидывайте все сюда. "
        "Все осматривается twitch модераторами!"
    )

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def forward_any(message: types.Message):
    # пересылаем сообщение админу (тебе)
    await bot.forward_message(
        chat_id=ADMIN_ID,
        from_chat_id=message.chat.id,
        message_id=message.message_id
    )

    # ответ пользователю
    await message.answer("✅ Отправлено, спасибо!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
