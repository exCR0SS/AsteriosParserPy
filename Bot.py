import telebot
import Parser
from settings import api_key
from settings import linkx55
from settings import linkx5
from settings import linkx7
from settings import linkx3
from settings import linkx1
from settings import bosses_respawn_days_setting

# ключ бота в файле settings, в github не отправляется
bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, f'Доступные команды:\n'
                                      f'Эпики серверов:\n'
                                      f'x55 - /bossX55\n'
                                      f'x5 - /bossX5\n'
                                      f'x7 - /bossX7\n'
                                      f'x3 - /bossX3\n'
                                      f'x1 - /bossX1')


@bot.message_handler(commands=['bossX55'])
def get_bosses_x55(message):
    bosses = Parser.get_bosses(linkx55)
    bot.send_message(message.chat.id, f'Список эпик боссов сервера х55 в порядке от ближайшего:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')


@bot.message_handler(commands=['bossX5'])
def get_bosses_x5(message):
    bosses = Parser.get_bosses(linkx5)
    bot.send_message(message.chat.id, f'Список эпик боссов сервера х5 в порядке от ближайшего:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')


@bot.message_handler(commands=['bossX7'])
def get_bosses_x7(message):
    bosses = Parser.get_bosses(linkx7)
    bot.send_message(message.chat.id, f'Список эпик боссов сервера х7 в порядке от ближайшего:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')


@bot.message_handler(commands=['bossX1'])
def get_bosses_x1(message):
    bosses = Parser.get_bosses(linkx1)
    bot.send_message(message.chat.id, f'Список эпик боссов сервера х1 в порядке от ближайшего:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')


@bot.message_handler(commands=['bossX3'])
def get_bosses_x3(message):
    bosses = Parser.get_bosses(linkx3)
    bot.send_message(message.chat.id, f'Список эпик боссов сервера х3 в порядке от ближайшего:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')


@bot.message_handler(commands=['author'])
def get_author(message):
    bot.send_message(message.chat.id, f'Автор: iCross')


@bot.message_handler(commands=['settings'])
def get_author(message):
    bot.send_message(message.chat.id,
                     f'Текущие настройки времени возрождения боссов (в днях):{bosses_respawn_days_setting}')


bot.polling()
