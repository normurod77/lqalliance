from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='5495640903:AAF0xm-QHCmQ-0UzSLiGY-PWRuJbZo5vqbs')
dp = Dispatcher(bot)
chat_id = -1001663008779

@dp.message_handler(commands=['reg'], commands_prefix='/')
async def rrrr(message: types.Message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == 1262601986  or message.reply_to_message.from_user.id == 674473647 or message.reply_to_message.from_user.id == 1232883508:
            f = message.reply_to_message.text
            d = str(f)
            rt = open('use.txt', 'r', encoding='utf-8')
            for sdf in rt:
                if not d in sdf:
                    if any(ch.isdigit() for ch in f) is True:
                        d = open('use.txt', 'a', encoding='utf-8')
                        f = message.reply_to_message.text
                        g = message.text
                        df = g[5:]
                        d.write(f'\n{f}-{df}.')
                        await bot.send_message(message.chat.id, "Клиент успешно зарегистрован")
                    else:
                        await bot.send_message(message.chat.id, 'вы ввели что-то другое')
                        return
                else:
                    await bot.send_message(message.chat.id, 'клиент уже существует')
                    return
        else:
            return
    else:
        await bot.send_message(message.chat.id, 'Это сообщение должно быть ответом на сообщения')
        return
executor.start_polling(dp, skip_updates=True)