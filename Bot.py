import telebot
import Parser
from settings import api_key


bot = telebot.TeleBot(api_key)
bosses = ParserOld.get_bosses()


# @bot.message_handler(commands=['start'])
# def start_bot(message):
#     bot.send_message(message.chat.id, f'Введите необходимый вариант (пока только для сервера: Hunter X55):\n'
#                                       f'1 - Время респа ВСЕХ ключевых эпик боссов (Антарас, Валакас, Баюм, Орфен, АК)\n')
#
#
# @bot.message_handler(content_types=['text'])
# def results(message):
#     if message.text.lower() == '1':
#         for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
#             bot.send_message(message.chat.id, f'{key}: {value}')
#     else:
#         bot.send_message(message.chat.id, 'Введите 1')


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, f'Список эпик боссов в порядке от ближайшего до удалённого:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')
    # else:
    #      bot.send_message(message.chat.id, 'Введите /start')

bot.polling()
