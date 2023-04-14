import telebot
import Parser
import settings
import datetime

# ключ бота в файле settings, в github не отправляется
bot = telebot.TeleBot(settings.api_key)


# pm2 start Bot.py --interpreter=python3 для запуска на сервере

# CHAT_BY_DATETIME = ()
# @bot.message_handler(func=lambda message: True)
# def on_request(message: telebot.types.Message):
#     text = 'Обработка!'
#     need_seconds = 300
#     current_time = datetime.datetime.now()
#     last_datetime = CHAT_BY_DATETIME.get(message.chat.id)
#
#     # Если первое сообщение (время не задано)
#     if not last_datetime:
#         CHAT_BY_DATETIME[message.chat.id] = current_time
#     else:
#         # Разница в секундах между текущим временем и временем последнего сообщения
#         delta_seconds = (current_time - last_datetime).total_seconds()
#
#         # Осталось ждать секунд перед отправкой
#         seconds_left = int(need_seconds - delta_seconds)
#
#         # Если время ожидания не закончилось
#         if seconds_left > 0:
#             text = f'Подождите {seconds_left} секунд перед выполнение этой команды'
#         else:
#             CHAT_BY_DATETIME[message.chat.id] = current_time
#
#     bot.reply_to(message, text)


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
    bosses = Parser.get_bosses(settings.linkx55)
    bot.send_message(message.chat.id, f'Список эпик боссов сервера х55 в порядке от ближайшего:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')


@bot.message_handler(commands=['bossX5'])
def get_bosses_x5(message):
    bosses = Parser.get_bosses(settings.linkx5)
    bot.send_message(message.chat.id, f'Список эпик боссов сервера х5 в порядке от ближайшего:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')


@bot.message_handler(commands=['bossX7'])
def get_bosses_x7(message):
    bosses = Parser.get_bosses(settings.linkx7)
    bot.send_message(message.chat.id, f'Список эпик боссов сервера х7 в порядке от ближайшего:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')


@bot.message_handler(commands=['bossX1'])
def get_bosses_x1(message):
    bosses = Parser.get_bosses(settings.linkx1)
    bot.send_message(message.chat.id, f'Список эпик боссов сервера х1 в порядке от ближайшего:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')


@bot.message_handler(commands=['bossX3'])
def get_bosses_x3(message):
    bosses = Parser.get_bosses(settings.linkx3)
    bot.send_message(message.chat.id, f'Список эпик боссов сервера х3 в порядке от ближайшего:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')


@bot.message_handler(commands=['author'])
def get_author(message):
    bot.send_message(message.chat.id, f'Автор: iCross')


@bot.message_handler(commands=['settings'])
def get_settings(message):
    bot.send_message(message.chat.id,
                     f'Текущие настройки времени возрождения боссов (в днях):{settings.bosses_respawn}')


# @bot.message_handler(regexp='/\d+')
# def get_fortress(message):
#     fortress = bot.send_message(message.chat.id, 'Название форта / замка?')
#     bot.register_next_step_handler(message, get_castles_fortress_tp(fortress, False))
# bot.reply_to(message.chat.id, )
# bot.send_message(message.chat.id,
#                  f'Телепорты к фортам через Alt + B:\n {settings.fortress_tp}')


# @bot.message_handler(commands=['castles'])
# def get_castle(message):
#     castle = bot.send_message(message.chat.id, 'Название замка?')
#     bot.register_next_step_handler(message, get_castles_fortress_tp(castle, True))


# @bot.message_handler(commands=['castle'])
# def get_siege_clanes(message):
#     castles = Parser.get_castles_siege()
#     bot.send_message(message.chat.id, f'Нажимаю на кнопку')

# @bot.message_handler(func=lambda message: message.reply_to_message != None)
# def reply_message_handler(message):
#     bot.send_message(chat_id=message.reply_to_message.from_user.id, text=message.text)

# @bot.message_handler(commands=['siegeTP'])
# def req_siegeTP(message):
#     user_request = message.text
#
#

#
# @bot.message_handler(commands=['siegeTP'])
# def get_castles_fortress_tp(message):
#     # user_request = message.text
#     castle_fortress = bot.reply_to(message, 'Название форта / замка?')
#     siegeTP = bot.register_next_step_handler(message, get_castles_fortress_tp(castle_fortress))
#     if siegeTP in settings.castles_tp:
#         return bot.reply_to(message, settings.castles_tp.values())
#     else:
#         return bot.reply_to(message, 'Такого замка / форта нет')





bot.polling()
