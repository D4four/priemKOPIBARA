import telebot

bot = telebot.TeleBot('6744225497:AAFV7H7f2l2bzDG5QQCkmkgOnhqKDMH6iEQ')
@bot.message_handler(commands=['start'])
def start(message):

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Перейти на сайт')
    markup.row(btn1)
    btn2 = telebot.types.KeyboardButton('Информация о пользователе')
    btn3 = telebot.types.KeyboardButton('Приветствие')
    markup.row(btn2, btn3)

    bot.send_message(message.chat.id, "Салют", reply_markup=markup)

#     bot.register_next_step_handler(message, onClick)
#
# def onClick(message):
#     if message.text.lower() == 'перейти на сайт':
#         markup = telebot.types.InlineKeyboardMarkup()
#         markup.add(telebot.types.InlineKeyboardButton(text="Открыть сайт", url="https://priem.guap.ru/"))
#
#         bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы открыть сайт:", reply_markup=markup)
#     elif message.text.lower() == 'информация о пользователе':
#         bot.send_message(message.chat.id, message)
#     elif message.text.lower() == 'приветствие':
#         bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['hello'])
def main(message):
    # bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    file = open('./photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file, caption=f'Привет, {message.from_user.first_name} {message.from_user.last_name}', parse_mode='Markdown')
@bot.message_handler(commands=['help', 'start'])
def help(message):
    bot.send_message(message.chat.id, '/help\n/hello\n/info\n/site')

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['site'])
def site(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text="Открыть сайт", url="https://priem.guap.ru/"))

    bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы открыть сайт:", reply_markup=markup)
@bot.message_handler(content_types=['photo'])
def getPhoto(message):

    bot.reply_to(message, 'Найс достижение, долбаеб')

@bot.message_handler()
def anyText(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower() == 'перейти на сайт':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text="Открыть сайт", url="https://priem.guap.ru/"))

        bot.send_message(message.chat.id, "Нажмите на кнопку, чтобы открыть сайт:", reply_markup=markup)
    elif message.text.lower() == 'информация о пользователе':
        bot.send_message(message.chat.id, message)
    elif message.text.lower() == 'приветствие':
        # bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
        file = open('./photo.jpg', 'rb')
        bot.send_photo(message.chat.id, file, caption=f'Привет, {message.from_user.first_name} {message.from_user.last_name}', parse_mode='Markdown')

bot.infinity_polling()