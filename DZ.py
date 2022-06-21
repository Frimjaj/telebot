def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "№1":
        dz1(bot, chat_id)

    elif ms_text == "№2":
        dz2(bot, chat_id)

    elif ms_text == "№3":
        dz3(bot, chat_id)

    elif ms_text == "№4":
        dz4(bot, chat_id)

    elif ms_text == "№5":
        dz5(bot, chat_id)

    elif ms_text == "№6":
        dz6(bot, chat_id)


# -----------------------------------------------------------------------
def dz1(bot, chat_id):
    bot.send_message(chat_id, text="Автора зовут Татьяна.\nВозраст: 18 лет.")


# -----------------------------------------------------------------------
def dz2(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько вам лет?", dz2_ResponseHandler)


def dz2_ResponseHandler(bot, chat_id, age_int):
    if age_int <= 0:
        bot.send_message(chat_id, text=f'Все ясно, автору (не Татьяне) 0 лет -_- ')

    elif 0 < age_int < 18:
        bot.send_message(chat_id, text=f'В детстве мама боялась, что я попаду в плохую компанию, а я вообще ни в какую не попал(а). класс..')

    elif age_int == 18:
        bot.send_message(chat_id, text=f'Вам столько же сколько и мне!! :)')

    elif 18 < age_int < 25:
        bot.send_message(chat_id, text=f'Да у вас, как я погляжу, появились седые волосы!! ')

    elif 25 <= age_int < 50:
        bot.send_message(chat_id, text=f'Да у вас определенно уже хрустят кости!! Вот у автора уже:) ')

    elif 50 <= age_int <= 100:
        bot.send_message(chat_id, text=f'Что вы делаете за моей программой?! Вы что ... ')

    elif age_int > 100:
        bot.send_message(chat_id, text=f'Вы вообще кто?? Призрак, домовой или вампир?!... ')

# -----------------------------------------------------------------------
def dz3(bot, chat_id):
    dz3_ResponseHandler = lambda message: bot.send_message(chat_id,
          f"Ваше имя {message.text}.\nВ нем: {len(message.text)} букв(ы)." 
              "\nВаше имя со 2-й до предпоследней буквы: " + message.text[1:-1] + "."
                   "\nВаше имя наоборот))) : " + message.text[::-1] + "."
                        "\nВаше имя с последними 3-мя буквами: " + message.text[-3:] + "."
                               "\nВаше имя с первыми 5-ю буквами: " + message.text[:5] + "."    )

    my_input(bot, chat_id, "Как тебя зовут?", dz3_ResponseHandler)

# -----------------------------------------------------------------------
def dz4(bot, chat_id):
    my_inputInt(bot, chat_id, "Сколько вам лет?", dz4_ResponseHandler)

def dz4_ResponseHandler(bot, chat_id, age_int):
    sum = 0
    mult = 1
    user_age_ex = age_int
    while user_age_ex > 0:
        temp = user_age_ex % 10
        sum = sum + temp
        mult = mult * temp
        user_age_ex = user_age_ex // 10

    bot.send_message(chat_id, text=f"Сумма чисел возраста: {sum}. А произведение: {mult} .")

# -----------------------------------------------------------------------
def dz5(bot, chat_id):
    dz5_ResponseHandler = lambda message: bot.send_message(chat_id,
          f"Ваше имя {message.text}.\nВаше имя заглавными буквами: {message.text.upper()}."
               "\nИмя маленькими буквами: " + message.text.lower() + "."                    
                         "\nИмя с заглавной буквы: " + str.capitalize(message.text) + "."
                               "\nИмя с маленькой буквы: " + message.text.swapcase() + "." )

    my_input(bot, chat_id, "Как тебя зовут?", dz5_ResponseHandler)


# -----------------------------------------------------------------------
def dz6(bot, chat_id):
    my_inputInt(bot, chat_id, "Решите задачу: 199-11**2*15 = ? ", dz6_ResponseHandler)

def dz6_ResponseHandler(bot, chat_id, task):
    if task == 1616:
        bot.send_message(chat_id, text="Верно! Ответ 1616.")
    else:
        bot.send_message(chat_id, text="Неверный ответ! (Ваш ответ: " + str(task) + ")" )

        # -----------------------------------------------------------------------
# -----------------------------------------------------------------------
def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)


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
                                 text="Это не то что мне нужно!!")
        my_inputInt(botQuestion, chat_id, txtQuestion, ResponseHandler)  # это не рекурсия, но очень похоже
        # у нас пара процедур, которые вызывают друг-друга, пока пользователь не введёт корректные данные,
        # и тогда этот цикл прервётся, и управление перейдёт "наружу", в ResponseHandler

# -----------------------------------------------------------------------
