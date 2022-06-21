def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Задание-1":
        dz1(bot, chat_id)

    elif ms_text == "Задание-2":
        dz2(bot, chat_id)

    elif ms_text == "Задание-3":
        dz3(bot, chat_id)

    elif ms_text == "Задание-4":
        dz4(bot, chat_id)

    elif ms_text == "Задание-5":
        dz5(bot, chat_id)

    elif ms_text == "Задание-6":
        dz6(bot, chat_id)


# -----------------------------------------------------------------------
def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)


# -----------------------------------------------------------------------
def dz1(bot, chat_id):
    dz1_ResponseHandler = lambda message: bot.send_message(chat_id, f"Ваше имя - {message.text}!")
    my_input(bot, chat_id, "Ваше имя?", dz1_ResponseHandler)


# -----------------------------------------------------------------------
def dz2(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько вам лет?", dz2_ResponseHandler)


def dz2_ResponseHandler(bot, chat_id, age_int):
    if age_int < 18:
        bot.send_message(chat_id, text=f"Дружок, у этого бота есть азартные игры. Спроси-ка разрешение у своих "
                                       f"родителей")  # Технически... Делаю то же самое что и задание 4... но пускай
    else:
        bot.send_message(chat_id, text=f"Никаких проблем, старичок. Просто пара азартных игр")


# -----------------------------------------------------------------------
def dz3(bot, chat_id):
    my_inputInt(bot, chat_id, "Я повторю ваш возраст несколько раз", dz3_ResponseHandler)

def dz3_ResponseHandler(bot, chat_id, age_int):
    for dz3_ResponseHandler in range (1, 6):
        bot.send_message(chat_id, f"{age_int}!")

# -----------------------------------------------------------------------
def dz4(bot, chat_id):
    dz4_Response = lambda message: bot.send_message(chat_id, f"Добро пожаловать {message.text}!")
    my_input(bot, chat_id, "Ваше имя?", dz4_Response)

    my_inputInt(bot, chat_id, "Сколько вам лет?", dz4_ResponseHandler)


def dz4_ResponseHandler(bot, chat_id, age_int):
    if age_int < 18:
        bot.send_message(chat_id, text=f"В азартные игры хочешь поиграть? Шалун, тебе ведь лишь {age_int}")
    elif age_int == 18:
        bot.send_message(chat_id, text=f"Прошу, вперёд, друг. Поиграй и расслабься, сессия только в июне")
    elif age_int > 18:
        bot.send_message(chat_id, text=f"Старичок, сходи сначала к доктору, а потом уж ботов тыкай")


# -----------------------------------------------------------------------
def dz5(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько вам лет?", dz5_ResponseHandler)


def dz5_ResponseHandler(bot, chat_id, age_int):
    bot.send_message(chat_id, text=f"О! тебе уже {age_int}! \nА через год будет уже {age_int + 1}!")


# -----------------------------------------------------------------------
def dz6(bot, chat_id):
    dz6_ResponseHandler = lambda message: bot.send_message(chat_id,
                                                           f"Добро пожаловать {message.text}! У тебя красивое имя, в нём {len(message.text)} букв!")
    my_input(bot, chat_id, "Как тебя зовут?", dz6_ResponseHandler)


# -----------------------------------------------------------------------
def my_inputInt(bot, chat_id, txt, ResponseHandler):
    # bot.send_message(chat_id, text=botGames.GameRPS_Multiplayer.name, reply_markup=types.ReplyKeyboardRemove())

    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, my_inputInt_SecondPart, botQuestion=bot, txtQuestion=txt,
                                   ResponseHandler=ResponseHandler)
    # bot.register_next_step_handler(message, my_inputInt_return, bot, txt, ResponseHandler)  # то-же самое, но короче


def my_inputInt_SecondPart(message, botQuestion, txtQuestion, ResponseHandler):
    chat_id = message.chat.id
    try:
        if message.content_type != "text":
            raise ValueError
        var_int = int(message.text)
        # данные корректно преобразовались в int, можно вызвать обработчик ответа, и передать туда наше число
        ResponseHandler(botQuestion, chat_id, var_int)
    except ValueError:
        botQuestion.send_message(chat_id,
                                 text="Можно вводить ТОЛЬКО целое число в десятичной системе исчисления (символами от 0 до 9)!\nПопробуйте еще раз...")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)  # это не рекурсия, но очень похоже