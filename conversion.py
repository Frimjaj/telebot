from googletrans import Translator


def get_text_messages(bot, cur_user, message):
    chat_id = message.chat.id
    ms_text = message.text

    if ms_text == "Переводчик":
        get_translate(bot, chat_id)

    elif ms_text == "Конвертер":
        convert(bot, chat_id)


def convert(bot, chat_id):
    my_inputInt(bot, chat_id, "Если вы ввели русский текст английскими буквами, я могу перевести. "
                              "Введите сообщение... ", convert_ResponseHandler)


def convert_ResponseHandler(bot, chat_id, perevod):
    layout = dict(zip(map(ord, '''qwertyuiop[]asdfghjkl;'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'''),
                      '''йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'''))

    return perevod.translate(layout)


def get_translate(bot, chat_id):
    my_inputInt(bot, chat_id, "Если вы ввели русский текст английскими буквами, я могу перевести. "
                              "Введите сообщение... ", get_translate1)


def get_translate1(bot, chat_id, words):
    translator = Translator()
    trans = words
    text2 = translator.translate(words)
    bot.send_message(chat_id, str.capitalize(text2.text))


# -----------------------------------------------------------------------
def my_input(bot, chat_id, txt, ResponseHandler):
    message = bot.send_message(chat_id, text=txt)
    bot.register_next_step_handler(message, ResponseHandler)


def my_inputInt(bot, chat_id, txt, ResponseHandler):
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

