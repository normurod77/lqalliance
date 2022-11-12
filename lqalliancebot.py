from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType, InlineKeyboardButton, InlineKeyboardMarkup, Message, callback_query
import time


bot = Bot(token='5716404046:AAGdCE_HoJSTqY2XWo47OD9Tj-sROKYPNcY')
dp = Dispatcher(bot)
chat_id = -1001814953183

@dp.message_handler(commands=['users'], commands_prefix='/')
async def rrrr(message: types.Message):
    fff = message.from_user.id
    d = str(fff)
    rt = open('use.txt', 'r', encoding='utf-8')
    for sdf in rt:
        if not d in sdf:
            t = InlineKeyboardButton(text='Список клиентов')
            r = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Вывести список', callback_data='f'))
            await message.answer('Список клиентов', reply_markup=r)
@dp.callback_query_handler(text='f')
async def yyy(callback : types.CallbackQuery):
    rt = open('use.txt', 'r', encoding='utf-8')
    sdd = rt.read()
    await bot.send_message(chat_id, f'Список клиентов\n{sdd}')

@dp.message_handler(commands=['start'], commands_prefix='/')
async def rr(message: types.Message):
    fff = message.from_user.id
    d = str(fff)
    rt = open('use.txt', 'r', encoding='utf-8')
    for sdf in rt:
        if d in sdf:
            await bot.send_message(message.from_user.id, "Здравствуйте, Вас приветствует бухгалтерский отдел компании «LQ ALLIANCE». Мы рады видеть вас в числе наших постоянных клиентов и готовы начать сотрудничество в бухгалтерском и юридическом сопровождении.\n\nКонтактные данные:\n📞 +998(98) 188-18-98\n📞 +998(91) 015-55-11\n\nС уважением, компания «LQ ALLIANCE»")


        else:
            await bot.send_message(message.chat.id, "Для получения доступа пожалуйста, обращайтесь по нижеперечисленными контактами: \n\nКонтактные данные:\n📞 +998(98) 188-18-98 \n📞 +998(91) 015-55-11\n\nС уважением, компания «LQ ALLIANCE»")
@dp.message_handler(content_types=ContentType.PHOTO)
async def p(message: Message):
    fff = message.from_user.id
    d = str(fff)
    rt = open('use.txt', 'r', encoding='utf-8')
    for sdf in rt:
        if d in sdf:
            s = time.time()
            f = time.ctime(s)
            r = f[11:13]
            d = int(r)
            w = f.lower()
            if 9 > d > 17 or 'sun' in w or 'sat' in w:
                fff = message.from_user.id
                d = str(fff)
                rt = open('use.txt', 'r', encoding='utf-8')
                for sdf in rt:
                    if d in sdf:
                        d = open('use.txt', 'r', encoding='utf-8')
                        fd = d.read()
                        ds = message.from_user.id
                        hh = str(ds)
                        f = hh[-2:-1]
                        dsa = fd[fd.find(f):fd.find(".")]
                        asds=dsa[3:]
                        asd =(f'*{asds}*')
                        await bot.send_photo(chat_id, message.photo[-1].file_id, f"ID:{message.chat.id} \n{asd} \n{message.caption} ", parse_mode='MARKDOWN')
                        await bot.send_message(message.chat.id,'Здравствуйте, меня зовут Бот-автоответчик. Рабочий день в компании LQ ALLIANCE закончился, но мы обязательно ответим на Ваше сообщение, как-только немного передохнём.\n\nP.S. Рабочий график пн-пт с 9:00 - 18:00\nС уважением команда компании LQ ALLIANCE')

            else:
                d = open('use.txt', 'r', encoding='utf-8')
                fd = d.read()
                ds = message.from_user.id
                hh = str(ds)
                f = hh[-2:-1]
                dsa = fd[fd.find(f):fd.find(".")]
                asds = dsa[3:]
                asd = (f'*{asds}*')
                await bot.send_photo(chat_id, message.photo[-1].file_id, f"ID:{message.chat.id}\n{asd}  \n{message.caption} ", parse_mode='MARKDOWN')

        else:
            if message.reply_to_message:
                if message.reply_to_message.from_user.id == 5716404046:
                    d = (message.reply_to_message.text)
                    f = message.reply_to_message.text
                    k = f[3:13]
                    await bot.send_photo(d[3:13], message.photo[-1].file_id)

                else:
                    return
@dp.message_handler(content_types=ContentType.VOICE)
async def p(message: Message):
    fff = message.from_user.id
    d = str(fff)
    rt = open('use.txt', 'r', encoding='utf-8')
    for sdf in rt:
        if d in sdf:
            s = time.time()
            f = time.ctime(s)
            r = f[11:13]
            d = int(r)
            w = f.lower()
            if 9 > d > 17 or 'sun' in w or 'sat' in w:
                d = open('use.txt', 'r', encoding='utf-8')
                fd = d.read()
                ds = message.from_user.id
                hh = str(ds)
                f = hh[-2:-1]
                dsa = fd[fd.find(f):fd.find(".")]
                asds = dsa[2:]
                asd = (f'*{asds}*')
                await bot.send_voice(chat_id, message.voice.file_id, f"ID:{message.chat.id}\n{asd}  ", parse_mode='MARKDOWN')
                await bot.send_message(message.chat.id,'Здравствуйте, меня зовут Бот-автоответчик. Рабочий день в компании LQ ALLIANCE закончился, но мы обязательно ответим на Ваше сообщение, как-только немного передохнём.\n\nP.S. Рабочий график пн-пт с 9:00 - 18:00\nС уважением команда компании LQ ALLIANCE')

            else:
                d = open('use.txt', 'r', encoding='utf-8')
                fd = d.read()
                ds = message.from_user.id
                hh = str(ds)
                f = hh[-2:-1]
                dsa = fd[fd.find(f):fd.find(".")]
                asds = dsa[2:]
                asd = (f'*{asds}*')
                await bot.send_voice(chat_id, message.voice.file_id, f"ID:{message.chat.id} \n{asd} ", parse_mode='MARKDOWN')

        else:
            if message.reply_to_message:
                if message.reply_to_message.from_user.id == 5716404046:
                    d = (message.reply_to_message.text)
                    f = message.reply_to_message.text
                    k = f[3:13]
                    await bot.send_message(chat_id, text=f"ID:{k}  \n \n{message.text}",
                                       parse_mode='MARKDOWN')
                    await bot.send_voice(d[3:13], message.voice.file_id)

                else:
                    return
@dp.message_handler(content_types=ContentType.DOCUMENT)
async def p(message: Message):
    fff = message.from_user.id
    d = str(fff)
    rt = open('use.txt', 'r', encoding='utf-8')
    for sdf in rt:
        if d in sdf:
            s = time.time()
            f = time.ctime(s)
            r = f[11:13]
            d = int(r)
            w = f.lower()
            if 9 > d > 17 or 'sun' in w or 'sat' in w:
                d = open('use.txt', 'r', encoding='utf-8')
                fd = d.read()
                ds = message.from_user.id
                hh = str(ds)
                f = hh[-2:-1]
                dsa = fd[fd.find(f):fd.find(".")]
                asds = dsa[3:]
                asd = (f'*{asds}*')
                await bot.send_document(chat_id, message.document.file_id, caption=f"ID:{message.chat.id} \n{asd} \n{message.caption} ", parse_mode='MARKDOWN')
                await bot.send_message(message.chat.id,
                               'Здравствуйте, меня зовут Бот-автоответчик. Рабочий день в компании LQ ALLIANCE закончился, но мы обязательно ответим на Ваше сообщение, как-только немного передохнём.\n\nP.S. Рабочий график пн-пт с 9:00 - 18:00\nС уважением команда компании LQ ALLIANCE')

            else:
                d = open('use.txt', 'r', encoding='utf-8')
                fd = d.read()
                ds = message.from_user.id
                hh = str(ds)
                f = hh[-2:-1]
                dsa = fd[fd.find(f):fd.find(".")]
                asds = dsa[3:]
                asd = (f'*{asds}*')
                await bot.send_document(chat_id, message.document, caption=f"ID:{message.chat.id} \n{asd} \n{message.caption} ", parse_mode='MARKDOWN')
        else:
            if message.reply_to_message:
                if message.reply_to_message.from_user.id == 5716404046:
                    d = (message.reply_to_message.text)
                    f = message.reply_to_message.text
                    k = f[3:13]
                    await bot.send_document(d[3:13], message.document.file_id)

                else:
                    return
@dp.message_handler()
async def h(message: types.Message):
    fff = message.from_user.id
    d = str(fff)
    rt = open('use.txt', 'r', encoding='utf-8')
    for sdf in rt:
        if d in sdf:
            s = time.time()
            f = time.ctime(s)
            r = f[11:13]
            d = int(r)
            w = f.lower()
            if 8 > d > 17 or 'sun' in w or 'sat' in w:
                d = open('use.txt', 'r', encoding='utf-8')
                fd = d.read()
                ds = message.from_user.id
                hh = str(ds)
                f = hh[-2:-1]
                dsa = fd[fd.find(f):fd.find(".")]
                asds = dsa[3:]
                asd = (f'*{asds}*')
                await bot.send_message(chat_id, text=f"ID:{message.chat.id} # \n{asd}   \n \n{message.text}", parse_mode='MARKDOWN')
                await bot.send_message(message.chat.id,
                                       f'{message.message_id}Здравствуйте, меня зовут Бот-автоответчик. Рабочий день в компании LQ ALLIANCE закончился, но мы обязательно ответим на Ваше сообщение, как-только немного передохнём.\n\nP.S. Рабочий график пн-пт с 9:00 - 18:00 \nС уважением команда компании LQ ALLIANCE')

            else:
                d = open('use.txt', 'r', encoding='utf-8')
                fd = d.read()
                ds = message.from_user.id
                hh = str(ds)
                f = hh[-2:-1]
                dsa = fd[fd.find(f):fd.find(".")]
                asds = dsa[3:]
                asd = (f'*{asds}*')
                await bot.send_message(chat_id,
                                       text=f"ID:{message.chat.id}    \n{asd} \n \n{message.text}",
                                       parse_mode='MARKDOWN')

        else:
            if message.reply_to_message:
                if message.reply_to_message.from_user.id == 5716404046:
                    if message.text == "20":
                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]
                        await bot.send_message(d[3:13],'Уважаемый клиент, ваше поручение будет выполнено в течении 20 минут.')
                    if message.text == "40":

                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await bot.send_message(d[3:13],'Уважаемый клиент, ваше поручение будет выполнено в течении 40 минут.')
                    if message.text == "60":

                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await bot.send_message(d[3:13],' Уважаемый клиент, ваше поручение будет выполнено в течении часа.')
                    if message.text == '1 день':

                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await bot.send_message(d[3:13],'Уважаемый клиент, ваше поручение будет выполнено завтра в течении рабочего дня.')
                    if message.text == '2 дня':
                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await bot.send_message(d[3:13],
                                           'Уважаемый клиент, ваше поручение будет выполнено в течении 2-х рабочих дней.')
                    if message.text == '3 дня':

                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await bot.send_message(d[3:13],'Уважаемый клиент, ваше поручение будет выполнено в течении 3-х рабочих дней.')
                    if not message.text == "20" and not message.text == "40" and not message.text == "60" and not message.text == "1 день" and not message.text == "2 дня" and not message.text == "3 дня" :
                        d = (message.reply_to_message.text)
                        f = message.reply_to_message.text
                        k = f[3:13]

                        await  bot.send_message(d[3:13], message.text)
                else:
                    d = message.from_user.id

                    inp_str = message.reply_to_message.text
                    num = ""
                    for c in inp_str:
                        if c.isdigit():
                            num = num + c
                            fff = message.from_user.id
                            d = str(fff)
                            rt = open('use.txt', 'r', encoding='utf-8')
                            for sdf in rt:
                                if num in sdf:
                                    if message.text == "20":

                                        d = (message.reply_to_message.text)
                                        f = message.reply_to_message.text
                                        k = f[3:13]

                                        await bot.send_message(num,'Уважаемый клиент, ваше поручение будет выполнено в течении 20 минут.')
                                    if message.text == "40":

                                        d = (message.reply_to_message.text)
                                        f = message.reply_to_message.text
                                        k = f[3:13]

                                        await bot.send_message(num,'Уважаемый клиент, ваше поручение будет выполнено в течении 40 минут.')
                                    if message.text == "60":

                                        d = (message.reply_to_message.text)
                                        f = message.reply_to_message.text
                                        k = f[3:13]

                                        await bot.send_message(num,' Уважаемый клиент, ваше поручение будет выполнено в течении часа.')
                                    if message.text == '1 день':

                                        d = (message.reply_to_message.text)
                                        f = message.reply_to_message.text
                                        k = f[3:13]

                                        await bot.send_message(num,'Уважаемый клиент, ваше поручение будет выполнено завтра в течении рабочего дня.')
                                    if message.text == '2 дня':
                                        d = (message.reply_to_message.text)
                                        f = message.reply_to_message.text
                                        k = f[3:13]

                                        await bot.send_message(num,
                                           'Уважаемый клиент, ваше поручение будет выполнено в течении 2-х рабочих дней.')
                                    if message.text == '3 дня':

                                        d = (message.reply_to_message.text)
                                        f = message.reply_to_message.text
                                        k = f[3:13]

                                        await bot.send_message(num,'Уважаемый клиент, ваше поручение будет выполнено в течении 3-х рабочих дней.')
                                    if not message.text == "20" and not message.text == "40" and not message.text == "60" and not message.text == "1 день" and not message.text == "2 дня" and not message.text == "3 дня" :
                                        d = (message.reply_to_message.text)
                                        f = message.reply_to_message.text
                                        k = f[3:13]

                                        await bot.send_message(num, message.text)
            else:
                return



executor.start_polling(dp, skip_updates=True)