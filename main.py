import telebot

bot = telebot.TeleBot('6744225497:AAFV7H7f2l2bzDG5QQCkmkgOnhqKDMH6iEQ')

@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, 'Заебали сюда писать..')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Нахуй ты сюда поступать хочешь?!..')

bot.infinity_polling()