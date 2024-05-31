import telebot
from telebot import types
import matplotlib.pyplot as plt
import imageio.v2 as imageio


bot = telebot.TeleBot("7435540349:AAFIHlHeVoHehdnqq5pM4EkNqgIzSTPZ-f4")

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋Давай")
    markup.add(btn1)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я твой карманный 🏋️ фитнес тренер, давай знакомиться!".format(
                         message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋Давай"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("💪 Программы тренировок")
        btn2 = types.KeyboardButton("🧑‍💻Полезные лайфхаки")
        btn3 = types.KeyboardButton("🤸 Техника выполнения упражнений")
        btn4 = types.KeyboardButton("🧮 Калькулятор калорий")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,
                         text="Что я умею? \n"
                               "💪 Раздел с тренировками. 👀 Я буду следить за твоими тренировками. ️ Если у тебя еще нет программы, я помогу её составить! \n"
                                        "😉Раздел с полезными советами по составлению тренировочного процесса\n️️"
                                        "🏋️Техника выполнения упражнений \n"
                                        "📅 Расчет суточной нормы калорий", reply_markup=markup)
    elif(message.text == "💪 Программы тренировок"):
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("👨‍🦰 Мужской", callback_data="male")
        btn2 = types.InlineKeyboardButton("👩‍🦰 Женский", callback_data="female")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Выберите ваш пол", reply_markup=markup)
    elif (message.text == "🤸 Техника выполнения упражнений"):
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("Жим лежа", callback_data="zhimlezha")
        btn2 = types.InlineKeyboardButton("Приседания", callback_data="prisedaniya")
        btn3 = types.InlineKeyboardButton("Бицепс", callback_data="biceps")
        btn4 = types.InlineKeyboardButton("Становая", callback_data="stanovaya")
        btn5 = types.InlineKeyboardButton("Разгибания на трицепс", callback_data="triceps")
        btn6 = types.InlineKeyboardButton("Махи", callback_data="mahi")
        btn7 = types.InlineKeyboardButton("Жим на плечи", callback_data="zhimplechi")
        btn8 = types.InlineKeyboardButton("Сгибания бедра", callback_data="bedro")
        btn9 = types.InlineKeyboardButton("Подтягивания", callback_data="pullups")
        btn10 = types.InlineKeyboardButton("Тяга блока", callback_data="tyaga")
        btn11 = types.InlineKeyboardButton("Пуловер", callback_data="pulover")
        btn12 = types.InlineKeyboardButton("Жим ногами", callback_data="zhimnogami")
        btn13 = types.InlineKeyboardButton("Скручивания", callback_data="press")
        btn14 = types.InlineKeyboardButton("Отжимания", callback_data="otzhim")
        btn15 = types.InlineKeyboardButton("Мертвая тяга", callback_data="mertvaya")

        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15)
        bot.send_message(message.chat.id, text="Выберите упражнение", reply_markup=markup)
    elif (message.text == "🧮 Калькулятор калорий"):
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("👨 Мужчина", callback_data="malee")
        btn2 = types.InlineKeyboardButton("👩 Женщина", callback_data="femalee")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Выберите ваш пол:", reply_markup=markup)
    elif (message.text == "🧑‍💻Полезные лайфхаки"):
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton("🥗 Как правильно составить рацион?", url='https://telegra.ph/Racion-pravilnogo-pitaniya-na-kazhdyj-den-05-30')
        btn2 = types.InlineKeyboardButton("💪 Принципы построения тренировочного процесса", url='https://telegra.ph/PRINCIPY-POSTROENIYA-TRENIROVOCHNOGO-PROCESSA-05-30')
        btn3 = types.InlineKeyboardButton("👨‍⚕️ 10 главных правил ЗОЖ", url='https://telegra.ph/10-samyh-glavnyh-pravil-zdorovogo-obraza-zhizni-05-30')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Ниже представлено несколько статей:", reply_markup=markup)
    elif(message.text == "Калькулятор калорий"):
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Мужчина", callback_data="malee")
        btn2 = types.InlineKeyboardButton("Женщина", callback_data="femalee")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Выберите ваш пол:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "male":
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton("🟢Легкий", callback_data="easym")
        btn2 = types.InlineKeyboardButton("🟡Средний", callback_data="mediumm")
        btn3 = types.InlineKeyboardButton("🔴Тяжелый", callback_data="hardm")
        btn4 = types.InlineKeyboardButton("Выбрать пол заново", callback_data="gender")
        markup.add(btn1, btn2, btn3, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите уровень сложности", reply_markup=markup)
    elif call.data == "gender":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("👨‍🦰Мужской", callback_data="male")
        btn2 = types.InlineKeyboardButton("👩‍🦰Женский", callback_data="female")
        markup.add(btn1, btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите ваш пол", reply_markup=markup)
    elif call.data == "female":
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton("🟢Легкий", callback_data="easyf")
        btn2 = types.InlineKeyboardButton("🟡Средний", callback_data="mediumf")
        btn3 = types.InlineKeyboardButton("🔴Тяжелый", callback_data="hardf")
        btn4 = types.InlineKeyboardButton("Выбрать пол заново", callback_data="gender")
        markup.add(btn1, btn2, btn3, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите ваш пол", reply_markup=markup)
    elif call.data == "easym":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Спина", callback_data="spinam")
        btn2 = types.InlineKeyboardButton("Грудь", callback_data="grudm")
        btn3 = types.InlineKeyboardButton("Ноги", callback_data="nogim")
        btn4 = types.InlineKeyboardButton("Плечи", callback_data="plechim")
        btn5 = types.InlineKeyboardButton("Руки", callback_data="rukim")
        btn6 = types.InlineKeyboardButton("Назад", callback_data="backm")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите мышечную группу", reply_markup=markup)
    elif call.data == "spinam":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="easym")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Legkaya-trenirovka-spiny-Muzhchiny-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Легкая тренировка Спины \n"
                                                                                                     "Подтягивания широким хватом — 4x8–10 повторений.\n"
                                                                                                    "Тяга верхнего блока к груди — 4x10–12 повторений.\n"
                                                                                                    "Тяга штанги в наклоне — 4x8–10 повторений.\n"
                                                                                                     "Гиперэкстензия — 4x12–15 повторений.", reply_markup=markup)

    elif call.data == "grudm":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="easym")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Legkaya-trenirovka-grudi-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Легкая тренировка Груди \n"
                                                                                                     "Жим гантелей лёжа — 4x10–12 повторений\n"
                                                                                                    "Сведение рук в тренажёре «бабочка» — 4x12–15 повторений.\n"
                                                                                                     "Отжимания — 4 подхода по максимальному количеству повторений.", reply_markup=markup)
    elif call.data == "nogim":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="easym")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Legkaya-trenirovka-nog-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Легкая тренировка Ног \n"
                                                                                                     "Приседания без веса — 4x20–25 повторений.\n"
                                                                                                     "Жим ногами в тренажёре — 4x10–12 повторений.\n"
                                                                                                     "Сведение ног в тренажёре — 4x12–15 повторений.", reply_markup=markup)
    elif call.data == "plechim":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="easym")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Legkaya-trenirovka-Plech-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Легкая тренировка Плеч \n"
                                                                                                     "Жим гантелей — 4x10–12 повторений\n"
                                                                                                     "Разведение гантелей в стороны — 4x10–12 повторений.\n"
                                                                                                     "Обратные отведения в тренажёре Peck-Deck — 4x12–15 повторений", reply_markup=markup)
    elif call.data == "rukim":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="easym")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Legkaya-trenirovka-ruk-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Легкая тренировка Рук \n"
                                                                                                     "Подтягивания обратным хватом — 3х10 повторений.\n"
                                                                                                     "Отжимания узким хватом — 3х10 повторений.\n"
                                                                                                     "Французский жим — 3х10 повторений.", reply_markup=markup)

    elif call.data == "backm":
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton("🟢Легкий", callback_data="easym")
        btn2 = types.InlineKeyboardButton("🟡Средний", callback_data="mediumm")
        btn3 = types.InlineKeyboardButton("🔴Тяжелый", callback_data="hardm")
        btn4 = types.InlineKeyboardButton("Выбрать пол заново", callback_data="gender")
        markup.add(btn1, btn2, btn3, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите уровень сложности", reply_markup=markup)
    elif call.data == "easyf":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Спина", callback_data="spinaf")
        btn2 = types.InlineKeyboardButton("Грудь", callback_data="grudf")
        btn3 = types.InlineKeyboardButton("Ноги", callback_data="nogif")
        btn4 = types.InlineKeyboardButton("Плечи", callback_data="plechif")
        btn5 = types.InlineKeyboardButton("Руки", callback_data="rukif")
        btn6 = types.InlineKeyboardButton("Назад", callback_data="backf")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите мышечную группу", reply_markup=markup)
    elif call.data == "spinaf":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="easyf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Legkaya-trenirovka-spiny-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Легкая тренировка Спины \n"
                                                                                                     "Гиперэкстензия — 3х10 повторений.\n"
                                                                                                     "Тяга верхнего блока — 3х10 повторений.\n"
                                                                                                     "Тяга нижнего блока — 3х10 повторений.", reply_markup=markup)
    elif call.data == "grudf":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="easyf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Legkaya-trenirovka-grudi-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Легкая тренировка Груди \n"
                                                                                                     "Отжимания от стены — 2x10–15 повторений.\n"
                                                                                                     "Жим гантелей лёжа на горизонтальной скамье — 3x10–12 повторений.\n"
                                                                                                     "Разведение гантелей лёжа на наклонной скамье — 3x10–12 повторений.", reply_markup=markup)
    elif call.data == "nogif":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="easyf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Legkaya-trenirovka-nog-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Легкая тренировка Ног \n"
                                                                                                     "Приседания без веса — 3X15–20 повторений\n"
                                                                                                     "Сгибание ног в тренажёре — 3x10–12 повторений.\n"
                                                                                                     "Подъём на носки стоя в тренажёре — 3x15–20 повторений.", reply_markup=markup)
    elif call.data == "plechif":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="easyf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Legkaya-trenirovka-plech-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Легкая тренировка Плеч \n"
                                                                                                     "Жим гантелей сидя — 3x10–12 повторений.\n"
                                                                                                     "Разведение гантелей в стороны стоя — 3x10–12 повторений.\n"
                                                                                                     "Обратные разведения в тренажёре Peck-Deck — 3x10–12 повторений.", reply_markup=markup)
    elif call.data == "rukif":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="easyf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Legkaya-trenirovka-ruk-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Легкая тренировка Рук \n"
                                                                                                     "Сгибание рук с гантелями — 3x10–12 повторений.\n"
                                                                                                     "Разгибание рук с гантелью из-за головы — 3x10–12 повторений.\n"
                                                                                                     "Сгибание рук на нижнем блоке — 3x10–12 повторений.", reply_markup=markup)

    elif call.data == "backf":
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn1 = types.InlineKeyboardButton("🟢Легкий", callback_data="easyf")
        btn2 = types.InlineKeyboardButton("🟡Средний", callback_data="mediumf")
        btn3 = types.InlineKeyboardButton("🔴Тяжелый", callback_data="hardf")
        btn4 = types.InlineKeyboardButton("Выбрать пол заново", callback_data="gender")
        markup.add(btn1, btn2, btn3, btn4)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите уровень сложности", reply_markup=markup)
    elif call.data == "mediumm":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Спина", callback_data="spinamm")
        btn2 = types.InlineKeyboardButton("Грудь", callback_data="grudmm")
        btn3 = types.InlineKeyboardButton("Ноги", callback_data="nogimm")
        btn4 = types.InlineKeyboardButton("Плечи", callback_data="plechimm")
        btn5 = types.InlineKeyboardButton("Руки", callback_data="rukimm")
        btn6 = types.InlineKeyboardButton("Назад", callback_data="backm")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите мышечную группу", reply_markup=markup)

    elif call.data == "spinamm":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="mediumm")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Srednyaya-trenirovka-spiny-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Средняя тренировка Спины \n"
                                                                                                     "Тяга штанги в наклоне — 3x–10 повторений.\n"
                                                                                                     "Тяга гантели одной рукой — 3x8–10 повторений на каждую сторону.\n"
                                                                                                     "Вертикальная тяга блока — 3x10–12 повторений.\n"
                                                                                                     "Шраги с гантелями — 3x10–12 повторений.", reply_markup=markup)
    elif call.data == "grudmm":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="mediumm")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Srednyaya-trenirovka-grudi-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Средняя тренировка Груди \n"
                                                                                                     "Жим штанги лёжа — 3x8–10 повторений.\n"
                                                                                                     "Разводка гантелей лёжа — 3x10–12 повторений.\n"
                                                                                                     "Сведение рук в кроссовере — 3x12–15 повторений.\n"
                                                                                                     "Пуловер с гантелью — 3x10–12 повторений.", reply_markup=markup)
    elif call.data == "nogimm":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="mediumm")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Srednyaya-trenirovka-nog-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Средняя тренировка Ног \n"
                                                                                                     "Приседания со штангой: 3x8–10 повторений.\n"
                                                                                                     "Жим ногами в тренажёре: 3x10–12 повторений.\n"
                                                                                                     "Сгибание ног в тренажёре: 3x10–12 повторений.\n"
                                                                                                     "Подъём на носки стоя в тренажёре: 3x15–20 повторений.", reply_markup=markup)
    elif call.data == "plechimm":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="mediumm")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Srednyaya-trenirovka-plech-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Средняя тренировка Плеч \n"
                                                                                                     "Жим гантелей сидя: 3x8–10 повторений.\n"
                                                                                                     "Разведение гантелей в стороны стоя: 3x10–12 повторений.\n"
                                                                                                     "Подъём гантелей через стороны в наклоне: 3x10–12 повторений.\n"
                                                                                                     "Шраги с гантелями: 3x10–12 повторений.", reply_markup=markup)
    elif call.data == "rukimm":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="mediumm")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Srednyaya-trenirovka-ruk-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Средняя тренировка Рук \n"
                                                                                                     "Сгибание рук со штангой: 3x8–10 повторений.\n"
                                                                                                     "Разгибание рук с гантелью из-за головы: 3x10–12 повторений.\n"
                                                                                                     "Сгибание рук на нижнем блоке: 3x10–12 повторений.\n"
                                                                                                     "Разгибание рук на верхнем блоке: 3x10–12 повторений.", reply_markup=markup)
    elif call.data == "hardm":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Спина", callback_data="spinamh")
        btn2 = types.InlineKeyboardButton("Грудь", callback_data="grudmh")
        btn3 = types.InlineKeyboardButton("Ноги", callback_data="nogimh")
        btn4 = types.InlineKeyboardButton("Плечи", callback_data="plechimh")
        btn5 = types.InlineKeyboardButton("Руки", callback_data="rukimh")
        btn6 = types.InlineKeyboardButton("Назад", callback_data="backm")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите мышечную группу", reply_markup=markup)

    elif call.data == "spinamh":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="hardm")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Tyazhelaya-trenirovka-Spiny-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тяжелая тренировка Спины \n"
                                                                                                     "Подтягивания широким хватом — 5x6–8 повторений.\n"
                                                                                                     "Тяга штанги в наклоне — 4x8–10 повторений.\n"
                                                                                                     "Тяга гантели одной рукой — 4x8–10 повторений.\n"
                                                                                                     "Гиперэкстензия — 3 подхода по максимуму.\n"
                                                                                                     "Вертикальная тяга блока — 3x10–12 повторений.", reply_markup=markup)
    elif call.data == "grudmh":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="hardm")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Tyazhelaya-trenirovka-grudi-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тяжелая тренировка Груди \n"
                                                                                                     "Жим штанги лёжа — 5x6–8 повторений."
                                                                                                     "Разведение гантелей лёжа — 4x8–10 повторений.\n"
                                                                                                     "Сведение рук в тренажёре «бабочка» — 4x10–12 повторений.\n"
                                                                                                     "Отжимания на брусьях — 3x10–12 повторений.\n"
                                                                                                     "Жим гантелей на наклонной скамье — 3x10–12 повторений.", reply_markup=markup)

    elif call.data == "nogimh":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="hardm")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Tyazhelaya-trenirovka-nog-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тяжелая тренировка Ног \n"
                                                                                                     "Приседания со штангой — 5x6–8 повторений."
                                                                                                     "Жим ногами — 4x8–10 повторений.\n"
                                                                                                     "Выпады с гантелями — 4x8–10 повторений.\n"
                                                                                                     "Сгибание ног в тренажёре — 3x10–12 повторений.\n"
                                                                                                     "Подъём на носки стоя — 3x10–12 повторений.", reply_markup=markup)
    elif call.data == "plechimh":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="hardm")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Tyazhelaya-trenirovka-plech-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тяжелая тренировка Плеч \n"
                                                                                                     "Жим гантелей сидя — 5x6–8 повторений."
                                                                                                     "Тяга штанги к подбородку — 4x8–10 повторений.\n"
                                                                                                     "Разведение гантелей в стороны — 4x8–10 повторений.\n"
                                                                                                     "Обратные отведения в тренажёре Peck-Deck — 3x10–12 повторений.\n"
                                                                                                     "Шраги с гантелями — 3x10–12 повторений.", reply_markup=markup)
    elif call.data == "rukimh":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="hardm")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Tyazhelaya-trenirovka-ruk-dlya-muzhchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тяжелая тренировка Рук \n"
                                                                                                     "Подтягивания обратным узким хватом — 5x6–8 повторений."
                                                                                                     "Французский жим со штангой — 4x8–10 повторений.\n"
                                                                                                     "Сгибание рук со штангой стоя — 4x8–10 повторений.\n"
                                                                                                     "Разгибание рук на верхнем блоке — 3x10–12 повторений.\n"
                                                                                                     "Сгибание рук с гантелями «молот» — 3x10–12 повторений.", reply_markup=markup)

    elif call.data == "mediumf":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Спина", callback_data="spinamf")
        btn2 = types.InlineKeyboardButton("Грудь", callback_data="grudmf")
        btn3 = types.InlineKeyboardButton("Ноги", callback_data="nogimf")
        btn4 = types.InlineKeyboardButton("Плечи", callback_data="plechimf")
        btn5 = types.InlineKeyboardButton("Руки", callback_data="rukimf")
        btn6 = types.InlineKeyboardButton("Назад", callback_data="backf")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите мышечную группу", reply_markup=markup)

    elif call.data == "spinamf":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="mediumf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Srednyaya-trenirovka-spiny-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Средняя тренировка Спины \n"
                                                                                                     "Подтягивания широким хватом — 3x8–10 повторений.\n"
                                                                                                     "Тяга верхнего блока к груди — 3x10–12 повторений.\n"
                                                                                                     "Гиперэкстензия — 3x15–20 повторений.\n"
                                                                                                     "Тяга нижнего блока к поясу сидя — 3x10–12 повторений.", reply_markup=markup)
    elif call.data == "grudmf":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="mediumf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Srednyaya-trenirovka-grudi-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Средняя тренировка Груди \n"
                                                                                                     "Жим гантелей лёжа — 3x8–10 повторений.\n"
                                                                                                     "Разводка гантелей лёжа — 3x10–12 повторений.\n"
                                                                                                     "Сведение рук в тренажёре — 3x15–20 повторений.\n"
                                                                                                     "Отжимания — 3 подхода по максимуму.", reply_markup=markup)
    elif call.data == "nogimf":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="mediumf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Srednyaya-trenirovka-nog-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Средняя тренировка Ног \n"
                                                                                                     "Приседания с гантелями — 3x10–12 повторений.\n"
                                                                                                     "Жим ногами в тренажёре  — 3x12–15 повторений.\n"
                                                                                                     "Сведение ног в тренажёре  — 3x20.\n"
                                                                                                     "Сгибание ног в тренажёре лёжа — 3x12–15 повторений.", reply_markup=markup)
    elif call.data == "plechimf":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="mediumf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Srednyaya-trenirovka-plech-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Средняя тренировка Плеч \n"
                                                                                                     "Жим гантелей сидя — 3x10–12 повторений.\n"
                                                                                                     "Разведение гантелей в стороны стоя — 3x12–15 повторений.\n"
                                                                                                     "Обратные отжимания от скамьи — 3x10–12 повторений.\n"
                                                                                                     "Подъём штанги к подбородку — 3x12–15 повторений.", reply_markup=markup)
    elif call.data == "rukimf":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="mediumf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Srednyaya-trenirovka-ruk-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Средняя тренировка Рук \n"
                                                                                                     "Французский жим с гантелями лёжа — 3x10–12 повторений.\n"
                                                                                                     "Сгибание рук с гантелями — 3x12–15 повторений.\n"
                                                                                                     "Отжимания от пола — 3 подхода по максимуму\n"
                                                                                                     "Разгибание рук на верхнем блоке — 3x12–15 повторений.", reply_markup=markup)
    elif call.data == "hardf":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Спина", callback_data="spinafh")
        btn2 = types.InlineKeyboardButton("Грудь", callback_data="grudfh")
        btn3 = types.InlineKeyboardButton("Ноги", callback_data="nogifh")
        btn4 = types.InlineKeyboardButton("Плечи", callback_data="plechifh")
        btn5 = types.InlineKeyboardButton("Руки", callback_data="rukifh")
        btn6 = types.InlineKeyboardButton("Назад", callback_data="backf")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите мышечную группу", reply_markup=markup)

    elif call.data == "spinafh":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="hardf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Tyazhelaya-trenirovka-spiny-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тяжелая тренировка Спины \n"
                                                                                                     "Вертикальная тяга блока — 4x10–12 повторений."
                                                                                                     "Тяга штанги в наклоне — 4x8–10 повторений.\n"
                                                                                                     "Тяга гантели одной рукой — 4x10–12 повторений на каждую руку.\n"
                                                                                                     "Гиперэкстензия — 4 подхода по максимуму.\n"
                                                                                                     "Планка — 4 подхода по максимальной продолжительности.", reply_markup=markup)
    elif call.data == "grudfh":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="hardf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Tyazhelaya-trenirovka-grudi-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тяжелая тренировка Груди \n"
                                                                                                     "Жим гантелей лёжа — 4x10–12 повторений."
                                                                                                     "Разводка гантелей лёжа — 4x12–15 повторений.\n"
                                                                                                     "Сведение рук в тренажёре — 4x12–15 повторений.\n"
                                                                                                     "Отжимания от пола — 4 подхода по максимуму.\n"
                                                                                                     "Пуловер с гантелью лёжа — 4x10–12 повторений.", reply_markup=markup)
    elif call.data == "nogifh":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="hardf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Tyazhelaya-trenirovka-nog-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тяжелая тренировка Ног \n"
                                                                                                     "Приседания со штангой — 4x8–10 повторений."
                                                                                                     "Жим ногами в тренажёре — 4x10–12 повторений.\n"
                                                                                                     "Выпады с гантелями — 4x10–12 повторений на каждую ногу.\n"
                                                                                                     "Сгибание ног в тренажёре — 4x12–15 повторений.\n"
                                                                                                     "Подъёмы на носки стоя — 4x20–25 повторений.", reply_markup=markup)
    elif call.data == "plechifh":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="hardf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Tyazhelaya-trenirovka-plech-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тяжелая тренировка Плеч \n"
                                                                                                     "Армейский жим — 4x0–12 повторений."
                                                                                                     "Разведение гантелей в стороны — 4x12–15 повторений.\n"
                                                                                                     "Тяга штанги к подбородку — 4x12–15 повторений.\n"
                                                                                                     "Махи гантелями в стороны — 4x12–15 повторений.\n"
                                                                                                     "Махи гантелями перед собой — 4x12–15 повторений.", reply_markup=markup)
    elif call.data == "rukifh":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Назад", callback_data="hardf")
        btn2 = types.InlineKeyboardButton("Подробнее...", url='https://telegra.ph/Tyazhelaya-trenirovka-ruk-dlya-zhenshchin-05-30')
        markup.add(btn1,btn2)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Тяжелая тренировка Рук \n"
                                                                                                     "Французский жим со штангой — 4x10–12 повторений."
                                                                                                     "Сгибание рук со штангой — 4x10–12 повторений.\n"
                                                                                                     "Разгибание рук на верхнем блоке — 4x12–15 повторений.\n"
                                                                                                     "Сгибание рук с гантелями — 4x12–15 повторений.\n"
                                                                                                     "Отжимания от пола — 4 подхода по максимуму.", reply_markup=markup)

    elif call.data == "zhimlezha":
        gif = open('zhim.gif', 'rb')
        markup = types.InlineKeyboardMarkup()
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        msg = bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Жим лежа \n"
                                                                    "1. Лягте на горизонтальную скамью. Используя средний хват (при котором в середине движения создаётся угол в 90 градусов между предплечьем и плечевой костью), снимите штангу со стоек и удерживайте на прямых руках. Это будет стартовая позицияа колени\n"
                                                                    "2. Сгибая руки в локтях, плавно опускайте штангу по направлению к середине груди и делайте вдох \n "
                                                                    "3. После короткой паузы в нижней точке выжимайте снаряд вверх, делая выдох. Сосредоточьтесь на том, чтобы максимально задействовать грудные мышцы при подъеме \n"
                                                                    "4. В верхней точке зафиксируйте руки, сократите грудные, задержитесь на секунду и снова медленно опускайте гриф. Лучше двигаться в два раза медленнее, чем при подъеме \n"
                                                                    "5.Повторите рекомендуемое количество раз и верните штангу на стойки ", reply_markup=markup)


    elif call.data.startswith("exercises:"):
        exercises_message_id = int(call.data.split(":")[1])
        bot.delete_message(call.message.chat.id, exercises_message_id)  # delete the GIF message
        bot.send_message(call.message.chat.id, "Выберите упражнение",
                         reply_markup=types.InlineKeyboardMarkup(row_width=1)
                         .add(types.InlineKeyboardButton("Жим лежа", callback_data="zhimlezha"),
                              types.InlineKeyboardButton("Приседания", callback_data="prisedaniya"),
                              types.InlineKeyboardButton("Бицепс", callback_data="biceps"),
                              types.InlineKeyboardButton("Становая", callback_data="stanovaya"),
                              types.InlineKeyboardButton("Разгибания на трицепс", callback_data="triceps"),
                              types.InlineKeyboardButton("Махи", callback_data="mahi"),
                              types.InlineKeyboardButton("Жим на плечи", callback_data="zhimplechi"),
                            types.InlineKeyboardButton("Сгибания бедра", callback_data="bedro"),
                            types.InlineKeyboardButton("Подтягивания", callback_data="pullups"),
                            types.InlineKeyboardButton("Тяга блока", callback_data="tyaga"),
                            types.InlineKeyboardButton("Пуловер", callback_data="pulover"),
                            types.InlineKeyboardButton("Жим ногами", callback_data="zhimnogami"),
                            types.InlineKeyboardButton("Скручивания", callback_data="press"),
                            types.InlineKeyboardButton("Отжимания", callback_data="otzhim"),
                            types.InlineKeyboardButton("Мертвая тяга", callback_data="mertvaya")))
    elif call.data == "biceps":
        markup = types.InlineKeyboardMarkup()
        gif = open('biceps.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Сгибания на бицепс \n"
                                                                    "1. Стойте ровно, удерживая штангу на ширине плеч обратным хватом. Локти держите ближе к корпусу. Это будет стартовая позиция\n"
                                                                    "2. На выдохе согните локти и поднимите вес, сокращая бицепс. Двигаться должны только предплечья, локти направлены строго в пол\n "
                                                                    "3. Продолжайте подъем до момента пока ладони не окажутся на уровне плеч. Выполняйте сгибание рук со штангой плавно, без рывковых движений. Задержитесь в верхней точке для пикового сокращения\n"
                                                                    "4. Медленно возвращайте штангу в стартовую позицию, делая вдох \n"
                                                                    "5. Повторите рекомендуемое количество раз", reply_markup=markup)
    elif call.data == "prisedaniya":
        markup = types.InlineKeyboardMarkup()
        gif = open('prised.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Приседания \n"
                                                                    "1. Расположите штангу на верхней части трапеций. Грудь расправлена, взгляд направлен вперед. Ноги поставьте на ширине плеч, слегка развернув носки наружу\n"
                                                                    "2. Начинайте опускаться вниз на вдохе, отводя таз назад и сгибая колени. Корпус наклоняется вперед минимально, спина ровная. Колени направляйте в стороны носков. Стопы не отрываются от пола \n "
                                                                    "3. Продолжайте движение, удерживая вес на пятках. В нижней точке бедра параллельны полу или чуть ниже\n"
                                                                    "4. С выдохом выпрямите ноги и вернитесь в исходное положение", reply_markup=markup)
    elif call.data == "stanovaya":
        markup = types.InlineKeyboardMarkup()
        gif = open('stanovaya.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Становая тяга \n"
                                                                    "1. Подойдите к штанге и поставьте ноги на ширине таза. Наклонитесь и обхватите гриф руками примерно на ширине плеч. Сделайте глубокий вдох, затем подсядьте и подтяните штангу к себе так, чтобы она коснулась голеней\n"
                                                                    "2. Запястья, локти и плечи находятся на одной линии над грифом. Взгляд направлен перед собой\n "
                                                                    "3. Раскройте грудную клетку и выпрямите спину, сводя лопатки. Поясница в нейтральном положении\n"
                                                                    "4. Теперь, направляя усилие через пятки, давите стопами в пол и разгибайте ноги, начиная поднимать вес\n"
                                                                    "5. Как только гриф пройдет уровень коленей, потяните штангу назад, сводя лопатки и направляя бедра вперед \n"
                                                                    "6. На вдохе медленно опускайте штангу на пол, отводя таз назад, сгибая ноги в коленях и продолжая держать ровную спину", reply_markup=markup)
    elif call.data == "triceps":
        markup = types.InlineKeyboardMarkup()
        gif = open('triceps.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Разгибания на трицепс с канатом \n"
                                                                    "1. Сядьте на горизонтальную скамью с поддержкой спины. Держите гантель на вытянутых руках над головой. Попросите партнера подать гантель, особенно если она тяжелая. Держите гантель ладонями за тыльную часть, обхватив пальцами. Это стартовая позиция. \n"
                                                                    "2. Направьте локти внутрь и держите их у головы. Руки должны быть перпендикулярны полу. Опускайте гантель по дуге, за голову, пока не коснетесь предплечьями бицепсов. Зафиксируйте руки и двигайте только предплечьями. Делайте вдох в этой фазе движения. \n "
                                                                    "3. Делая выдох, вернитесь в стартовую позицию, поднимая гантель за счет трицепсов. \n"
                                                                    "4. Выполните рекомендуемое количество повторений.", reply_markup=markup)
    elif call.data == "mahi":
        markup = types.InlineKeyboardMarkup()
        gif = open('mahi.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Отведения на плечи сидя \n"
                                                                    "1. Возьмите пару гантелей, стопы плотно прижаты к полу. Удерживайте гантели по бокам на прямых руках так, чтобы ладони были направлены внутрь. Это будет стартовая позиция\n"
                                                                    "2. Сохраняя корпус неподвижным, поднимайте гантели через стороны. Держите руки слегка согнутыми в локтях и поверните запястья так, будто наливаете воду в стакан. Продолжайте, пока руки не достигнут параллели с полом. Сделайте паузу в верхней точке движения и выдохните\n "
                                                                    "3. Медленно опускайте гантели в стартовую позицию, делая вдох\n"
                                                                    "4. Повторите рекомендуемое количество раз", reply_markup=markup)
    elif call.data == "zhimplechi":
        markup = types.InlineKeyboardMarkup()
        gif = open('zhimplechi.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Жим гантелей \n"
                                                                    "1. Поставьте ноги на ширине плеч и возьмите гантели. Поднимите их вверх так, чтобы угол в локтях составил 90 градусов. Это стартовая позиция.\n"
                                                                    "2. Придерживайтесь техники, не помогайте ногами и не отклоняйтесь назад. Одновременно поднимите гантели над головой. \n "
                                                                    "3. Сделайте паузу. Медленно возвращайтесь в стартовую позицию. \n"
                                                                    "4. Выполните заданное число повторений.", reply_markup=markup)
    elif call.data == "bedro":
        markup = types.InlineKeyboardMarkup()
        gif = open('bedro.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Сгибания бедра лежа \n"
                                                                    "1. Лягте на тренажер лицом вниз, поместив лодыжки под валик (чуть ниже икроножных). Лучше использовать тренажер для сгибаний ног, в котором подушки расположены под углами, чем ровный, так как под углом больше задействован бицепс бедра\n"
                                                                    "2. Прижмите корпус к скамье тренажера. Ноги выпрямлены в коленях, руками можно держаться за ручки по бокам. Носки направлены в пол. Это будет стартовая позиция\n "
                                                                    "3. Делая выдох, согните ноги. Не отрывайте бедра от тренажера и не прогибайте поясницу. Как только достигнете пиковой точки, задержитесь на секунду\n"
                                                                    "4. Делая вдох, плавно возвращайте ноги в стартовую позицию\n"
                                                                    "5. Повторите рекомендуемое число раз", reply_markup=markup)
    elif call.data == "pullups":
        markup = types.InlineKeyboardMarkup()
        gif = open('pullups.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Подтягивания \n"
                                                                    "1. Возьмитесь за перекладину прямым хватом. Примечание: При широком хвате руки расположены шире плеч, при среднем — на ширине плеч, а при узком — уже ширины плеч\n"
                                                                    "2. Держитесь за перекладину рекомендуемым хватом. Подав грудь вперед, создайте прогиб в пояснице. Это стартовая позиция\n "
                                                                    "3. Сводите лопатки, сокращая мышцы спины и сгибая руки в локтях. Подтягивайте корпус вверх, пока не коснетесь перекладины верхом груди. Отводите плечи и локти назад. Сделайте выдох в верхней точке. Верхняя часть тела остается неподвижной, двигаются только руки\n"
                                                                    "4. После секундной паузы в верхней точке сделайте выдох и медленно опускайтесь в стартовую позицию, выпрямляя руки и растягивая широчайшие мышцы спины\n"
                                                                    "5. Повторите упражнение рекомендуемое число раз", reply_markup=markup)
    elif call.data == "tyaga":
        markup = types.InlineKeyboardMarkup()
        gif = open('tyaga.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Тяга верхнего блока \n"
                                                                    "1. Присоедините широкую рукоять к верхнему блоку и настройте фиксатор для ног под свой рост. Он поможет не отрываться от сиденья под воздействием противовеса\n"
                                                                    "2. Возьмитесь за рукоять ладонями сверху, используя хват шире плеч. Удерживая рукоять на прямых руках, сядьте на сидение, разместив колени под валиком. Наклонитесь назад приблизительно на 30 градусов. Выведите грудь вперед, создавая небольшой прогиб в пояснице. Это стартовая позиция\n "
                                                                    "3. Делая выдох, сводите лопатки и сгибайте руки в локтях, опуская рукоять по направлению к верху груди. Корпус остается неподвижным. Не помогайте опускать вес предплечьями, используйте их, чтобы удерживать рукоять\n"
                                                                    "4. В нижней точке движения сделайте секундную паузу. Затем медленно возвращайтесь в стартовую позицию со вдохом. Руки выпрямлены, а широчайшие растянуты\n"
                                                                    "5. Сделайте рекомендуемое количество повторений", reply_markup=markup)
    elif call.data == "pulover":
        markup = types.InlineKeyboardMarkup()
        gif = open('pulover.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Пуловер \n"
                                                                    "1. Возьмите прямую рукоять верхнего блока хватом шире плеч. Используйте прямой хват (ладони направлены вниз). Отойдите на один-два шага назад, наклонитесь вперед на 30 градусов, держа руки слегка согнутыми в локтях на уровне глаз. Это стартовая позиция\n"
                                                                    "2. Сделайте выдох и тяните рукоять вниз до уровня бедер, сокращая широчайшие\n "
                                                                    "3. Сохраняя руки ровными, плавно возвращайтесь в стартовую позицию на вдохе\n"
                                                                    "4. Повторите рекомендуемое количество раз", reply_markup=markup)
    elif call.data == "zhimnogami":
        markup = types.InlineKeyboardMarkup()
        gif = open('zhimnogami.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Сгибания на бицепс \n"
                                                                    "1. Настройте тренажер так, чтобы расположиться в нем, согнув ноги в коленях.\n"
                                                                    "2. Выбрав корректный вес, лягте в тренажер, согнув ноги в коленях так, чтобы бедра были ниже параллели относительно платформы. Колени не должны выходить за уровень носков. Голова и спина должны быть расположены на спинке тренажера. Плечи находятся под валиками.\n "
                                                                    "3. Возьмитесь руками за рукояти по сторонам тренажера. Поставьте ноги на ширине плеч и разверните носки наружу. Это стартовая позиция.\n"
                                                                    "4. Делая выдох, разогните ноги, направляя усилие через стопы. Полностью выпрямитесь, сокращая квадрицепсы. Сделайте паузу в этом положении. Поскольку бедра находятся ниже параллели, вы можете надавить на них руками, чтобы выполнить первый повтор\n"
                                                                    "5. Делая вдох, медленно присядьте вниз, но не полностью, а так, чтобы бедра были параллельны платформе. Ноги будут согнуты под углом 90 градусов.\n"
                                                                    "6. Выполните рекомендуемое количество повторений.\n"
                                                                    "7. Спина и голова всегда должны быть прижаты к спинке тренажера.", reply_markup = markup)
    elif call.data == "press":
        markup = types.InlineKeyboardMarkup()
        gif = open('press.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Скручивания \n"
                                                                    "1. Лягте на спину, поставив ноги на пол на ширине плеч. Удерживайте согнутые руки у висков, направляя локти в стороны. Не скрещивайте пальцы за головой\n"
                                                                    "2. Прижмите поясницу к полу, чтобы снять с нее нагрузку и сильнее включить мышцы живота. Слегка округлите грудную клетку и на выдохе начните скручиваться, поднимая плечи и сокращая пресс\n "
                                                                    "3. Плечи двигаются по направлению к тазу, поясница также прижата к полу. В верхней точке максимально напрягите мышцы живота и удерживайте это положение одну секунду. Сосредоточьтесь на том, чтобы выполнять движение медленно и подконтрольно, не используя инерцию\n"
                                                                    "4. После паузы медленно опускайтесь в стартовую позицию, делая вдох\n"
                                                                    "5. Повторите рекомендуемое количество раз", reply_markup=markup)
    elif call.data == "otzhim":
        markup = types.InlineKeyboardMarkup()
        gif = open('otzhim.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Сгибания на бицепс \n"
                                                                    "1. Примите упор лежа, поставив руки чуть шире плеч, при этом удерживая корпус на вытянутых руках. На вдохе опускайтесь вниз, сгибая локти, практически до касания грудью пола \n"
                                                                    "2. Теперь сделайте выдох и поднимайте корпус вверх, в стартовую позицию, сокращая грудные мышцы\n "
                                                                    "3. После короткой паузы в верхней точке снова опуститесь вниз\n"
                                                                    "4. Выполните заданное количество повторений", reply_markup=markup)
    elif call.data == "mertvaya":
        markup = types.InlineKeyboardMarkup()
        gif = open('mertvaya.gif', 'rb')
        btn_back = types.InlineKeyboardButton("Назад", callback_data=f"exercises:{call.message.message_id}")
        markup.add(btn_back)
        bot.send_animation(call.message.chat.id, gif, caption="Техника выполнения упражнения: Сгибания на бицепс \n"
                                                                    "1. Примите исходное положение стоя. Руки опущены вниз и удерживают гантели. Лопатки сведены, грудь расправлена, пресс напряжен. Взгляд направлен перед собой \n"
                                                                    "2. Наклонитесь вперед, сгибаясь в тазобедренном суставе и удерживая ноги прямыми. Сделайте вдох. Важно: Если гибкости недостаточно и держать ноги прямыми не получается, можно слегка их согнуть, чтобы снять напряжение в подколенных связках. В стандартной амплитуде наклоняются вниз, пока гантели не опустятся до уровня середины голени\n "
                                                                    "3. Поднимайте туловище вверх, делая выдох. По ходу всего движения держите гантели близко к ногам. Допускается легкое скольжение гантелей по бедрам. Важно: При выполнении упражнения спина прямая как при опускании туловища, так и при его подъеме. Ни в коем случае не округляйте поясницу, иначе на позвоночник ложится нагрузка, которая может спровоцировать травму\n"
                                                                    "4. Выполните необходимое количество повторений", reply_markup=markup)

    elif call.data == "malee":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Минимальный", callback_data="minmale")
        btn2 = types.InlineKeyboardButton("Низкий", callback_data="lowmale")
        btn3 = types.InlineKeyboardButton("Умеренный", callback_data="mediummale")
        btn4 = types.InlineKeyboardButton("Высокий", callback_data="highmale")
        btn5 = types.InlineKeyboardButton("Экстремальный", callback_data="extrememale")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите уровень активности", reply_markup=markup)
    elif call.data == "femalee":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton("Минимальный", callback_data="minfemale")
        btn2 = types.InlineKeyboardButton("Низкий", callback_data="lowfemale")
        btn3 = types.InlineKeyboardButton("Умеренный", callback_data="mediumfemale")
        btn4 = types.InlineKeyboardButton("Высокий", callback_data="highfemale")
        btn5 = types.InlineKeyboardButton("Экстремальный", callback_data="extremefemale")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите уровень активности", reply_markup=markup)
    elif call.data == "minmale":
        activity_level = 1.2
        bot.send_message(call.message.chat.id, "Введите ваш вес в килограммах.")
        bot.register_next_step_handler(call.message, get_height, "malee", activity_level)
    elif call.data == "lowmale":
        activity_level = 1.375
        bot.send_message(call.message.chat.id, "Введите ваш вес в килограммах.")
        bot.register_next_step_handler(call.message, get_height, "malee", activity_level)
    elif call.data == "mediummale":
        activity_level = 1.55
        bot.send_message(call.message.chat.id, "Введите ваш вес в килограммах.")
        bot.register_next_step_handler(call.message, get_height, "malee", activity_level)
    elif call.data == "highmale":
        activity_level = 1.7
        bot.send_message(call.message.chat.id, "Введите ваш вес в килограммах.")
        bot.register_next_step_handler(call.message, get_height, "malee", activity_level)
    elif call.data == "extrememale":
        activity_level = 1.9
        bot.send_message(call.message.chat.id, "Введите ваш вес в килограммах.")
        bot.register_next_step_handler(call.message, get_height, "malee", activity_level)
    elif call.data == "minfemale":
        activity_level = 1.2
        bot.send_message(call.message.chat.id, "Введите ваш вес в килограммах.")
        bot.register_next_step_handler(call.message, get_height, "femalee", activity_level)
    elif call.data == "lowfemale":
        activity_level = 1.375
        bot.send_message(call.message.chat.id, "Введите ваш вес в килограммах.")
        bot.register_next_step_handler(call.message, get_height, "femalee", activity_level)
    elif call.data == "mediumfemale":
        activity_level = 1.55
        bot.send_message(call.message.chat.id, "Введите ваш вес в килограммах.")
        bot.register_next_step_handler(call.message, get_height, "femalee", activity_level)
    elif call.data == "highfemale":
        activity_level = 1.7
        bot.send_message(call.message.chat.id, "Введите ваш вес в килограммах.")
        bot.register_next_step_handler(call.message, get_height, "femalee", activity_level)
    elif call.data == "extremefemale":
        activity_level = 1.9
        bot.send_message(call.message.chat.id, "Введите ваш вес в килограммах.")
        bot.register_next_step_handler(call.message, get_height, "femalee", activity_level)

def get_height(message, sex, activity_level):
    try:
        weight = float(message.text)
        if weight <= 0:
            bot.send_message(message.chat.id, "Ошибка! Вес должен быть больше 0.")
            bot.register_next_step_handler(message, get_height, sex, activity_level)
        else:
            bot.send_message(message.chat.id, "Введите ваш рост в сантиметрах.")
            bot.register_next_step_handler(message, get_age, weight, sex, activity_level)
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка! Введите число.")
        bot.register_next_step_handler(message, get_height, sex, activity_level)
def get_age(message, weight, sex, activity_level):
    try:
        height = float(message.text)
        if height <= 0:
            bot.send_message(message.chat.id, "Ошибка! Рост должен быть больше 0.")
            bot.register_next_step_handler(message, get_age, weight, sex, activity_level)
        else:
            bot.send_message(message.chat.id, "Введите ваш возраст в годах.")
            bot.register_next_step_handler(message, calculate_calories, weight, height, sex, activity_level)
    except ValueError:
        bot.send_message(message.chat.id, "Ошибка! Введите число.")
        bot.register_next_step_handler(message, get_age, weight, sex, activity_level)

def calculate_calories(message, weight, height, sex, activity_level):
    age = message.text
    if float(age) <= 0:
        bot.send_message(message.chat.id, "Ошибка! Возраст должен быть больше 0.")
        bot.register_next_step_handler(message, calculate_calories, weight, height, sex, activity_level)
    else:
        weight = float(weight)
        height = float(height)
        age = float(age)
        if sex == "malee":
            bmr = 66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * age)
        elif sex == "femalee":
            bmr = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)
        calories = bmr * activity_level
        bot.send_message(message.chat.id, f"Ваша норма калорий: {calories:.2f} ккал")


bot.polling(none_stop=True)