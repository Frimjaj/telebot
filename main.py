import telebot
from telebot import types
from mg import get_map_cell
import MenuBot
from MenuBot import Menu

bot = telebot.TeleBot('5196769100:AAExRJdgXE__e0ZiTPCPE1u_OzYLC9069js')


@bot.message_handler(commands="start")
def command(message):
    chat_id = message.chat.id
    txt_message = f"Приветик, {message.from_user.first_name}! Я Кои - бот, но у меня есть много интересного для "
                                      "тебя!."
    bot.send_messade(chat_id, text=txt_message, reply_markup=Menu.getMenu(chat_id, "Главное меню").markup)
    bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEE1Cdij94Gnb3nZgqxGqPTfGbV0dF_IgAC4woAAnaMGEvwm2uAGaypPCQE')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text

    @bot.message_handler(content_types=['sticker'])
    def get_messages(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Это " + message.content_type)

        sticker = message.sticker
        bot.send_message(message.chat.id, sticker)

        # глубокая инспекция объекта
        # import inspect,pprint
        # i = inspect.getmembers(sticker)
        # pprint.pprint(i)

    # -----------------------------------------------------------------------

    @bot.message_handler(content_types=['audio'])
    def get_messages(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Это " + message.content_type)

        audio = message.audio
        bot.send_message(chat_id, audio)

    # -----------------------------------------------------------------------

    @bot.message_handler(content_types=['voice'])
    def get_messages(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Это " + message.content_type)

        voice = message.voice
        bot.send_message(message.chat.id, voice)

    # -----------------------------------------------------------------------

    @bot.message_handler(content_types=['photo'])
    def get_messages(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Это " + message.content_type)

        photo = message.photo
        bot.send_message(message.chat.id, photo)

    # -----------------------------------------------------------------------

    @bot.message_handler(content_types=['video'])
    def get_messages(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Это " + message.content_type)

        video = message.video
        bot.send_message(message.chat.id, video)

    # -----------------------------------------------------------------------

    @bot.message_handler(content_types=['document'])
    def get_messages(message):
        chat_id = message.chat.id
        mime_type = message.document.mime_type
        bot.send_message(chat_id, "Это " + message.content_type + " (" + mime_type + ")")

        document = message.document
        bot.send_message(message.chat.id, document)
        if message.document.mime_type == "video/mp4":
            bot.send_message(message.chat.id, "This is a GIF!")

    # -----------------------------------------------------------------------

    @bot.message_handler(content_types=['location'])
    def get_messages(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Это " + message.content_type)

        location = message.location
        bot.send_message(message.chat.id, location)

    # -----------------------------------------------------------------------

    @bot.message_handler(content_types=['contact'])
    def get_messages(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Это " + message.content_type)

        contact = message.contact
        bot.send_message(message.chat.id, contact)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        chat_id = message.chat.id
        ms_text = message.text

        if ms_text == "приветик" or ms_text == "привет" or ms_text == "Привет" or ms_text == "прив":
            bot.send_message(message.chat.id, ms_text)
            bot.send_sticker(message.chat.id,
                             "CAACAgIAAxkBAAEE1L9ikH1k2oYiDEmJrWwBzVKdBNvvHgACCQwAApg_EUuYbJsXCCcikSQE")

    cur_user = MenuBot.Users.getUser(chat_id)
    if cur_user is None:
        cur_user = MenuBot.Users(chat_id, message.json["from"])
        subMenu = menuBot.goto_menu(bot, chat_id,
                                    ms_text)  # попытаемся использовать текст как команду меню, и войти в него

        cur_menu = Menu.getCurMenu(chat_id)
        if cur_menu is not None and ms_text in cur_menu.buttons:  # проверим, что команда относится к текущему меню
            module = cur_menu.module

        subMenu = menuBot.goto_menu(bot, chat_id,
                                    ms_text)  # попытаемся использовать текст как команду меню, и войти в него
        if subMenu is not None:
            # Проверим, нет ли обработчика для самого меню. Если есть - выполним нужные команды
            if subMenu.name == "Игра в 21":
                game21 = botGames.newGame(chat_id, botGames.Game21(jokers_enabled=True))  # создаём новый экземпляр игры
                text_game = game21.get_cards(2)  # просим 2 карты в начале игры
                bot.send_media_group(chat_id, media=game21.mediaCards)  # получим и отправим изображения карт
                bot.send_message(chat_id, text=text_game)

            elif subMenu.name == "Игра КНБ":
                gameRPS = botGames.newGame(chat_id,
                                           botGames.GameRPS())  # создаём новый экземпляр игры и регистрируем его
                bot.send_photo(chat_id, photo=gameRPS.url_picRules, caption=gameRPS.text_rules, parse_mode='HTML')

            return  # мы вошли в подменю, и дальнейшая обработка не требуется

        if module != "":
            exec(module + ".get_text_messages(bot, cur_user, message)")

    if ms_text == "Пользователи":
        send_help(bot, chat_id)

    else:  # ======================================= случайный текст
        bot.send_message(chat_id, text='Это что такое  ➡  "' + ms_text + '" ? ')
        menuBot.goto_menu(bot, chat_id, "Главное меню")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # если требуется передать один или несколько параметров в обработчик кнопки,
    # используйте методы Menu.getExtPar() и Menu.setExtPar()
    # call.data это callback_data, которую мы указали при объявлении InLine-кнопки
    # После обработки каждого запроса вызовете метод answer_callback_query(), чтобы Telegram понял, что запрос обработан
    chat_id = call.message.chat.id
    message_id = call.message.id
    cur_user = menuBot.Users.getUser(chat_id)
    if cur_user is None:
        cur_user = menuBot.Users(chat_id, call.message.json["from"])

    tmp = call.data.split("|")
    menu = tmp[0] if len(tmp) > 0 else ""
    cmd = tmp[1] if len(tmp) > 1 else ""
    par = tmp[2] if len(tmp) > 2 else ""


def send_help(bot, chat_id):
    bot.send_message(chat_id, "Автор: Ульянова Татьяна")
    markup = types.InlineKeyboardMarkup()
    # btn1 = types.InlineKeyboardButton(text="Напишите автору", url="https://t.me/oviraxo")
    # markup.add(btn1)

bot.polling(none_stop=True, interval=0)
