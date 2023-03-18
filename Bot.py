import telebot
import Parser
import settings

# ключ бота в файле settings, в github не отправляется
bot = telebot.TeleBot(settings.api_key)


# pm2 start Bot.py --interpreter=python3 для запуска на сервере

# last_message = {}
# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     if message.from_user.id not in last_message:
#         last_message[message.from_user.id] = message.date - 5
#         print(last_message)
#     if message.date - last_message[message.from_user.id] > 5:
#         bot.reply_to(message, message.text)
#         last_message[message.from_user.id] = message.date
#         print(last_message)


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
def get_author(message):
    bot.send_message(message.chat.id,
                     f'Текущие настройки времени возрождения боссов (в днях):{settings.bosses_respawn}')


@bot.message_handler(commands=['fortress'])
def get_author(message):
    fort = bot.send_message(message.chat.id, 'Название форта?')
    result = bot.register_next_step_handler(fort, get_castles_fortress_tp(message.chat.id, False))
    # bot.reply_to(message.chat.id, )
    print(result)
    # bot.send_message(message.chat.id,
    #                  f'Телепорты к фортам через Alt + B:\n {settings.fortress_tp}')


@bot.message_handler(commands=['castles'])
def get_author(message):
    fort = bot.send_message(message.chat.id, 'Название замка?')
    bot.register_next_step_handler(fort, get_castles_fortress_tp(message.chat.id, True))


# @bot.message_handler(commands=['castle'])
# def get_siege_clanes(message):
#     castles = Parser.get_castles_siege()
#     bot.send_message(message.chat.id, f'Нажимаю на кнопку')

# @bot.message_handler(func=lambda message: message.reply_to_message != None)
# def reply_message_handler(message):
#     bot.send_message(chat_id=message.reply_to_message.from_user.id, text=message.text)


@bot.message_handler(content_types=['text'])
def get_castles_fortress_tp(message, castle):
    user_request = message
    if castle is True:
        if user_request in settings.castles_tp:
            return bot.reply_to(message, settings.castles_tp.values())
        # else:
        #     return bot.reply_to(message, 'Такого замка нет')
    else:
        if user_request in settings.fortress_tp:
            return bot.reply_to(message, settings.fortress_tp.values())
        # else:
        #     return bot.reply_to(message, 'Такого форта нет')


bot.polling()
