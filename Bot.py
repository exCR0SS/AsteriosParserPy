import telebot
import Parser
from settings import api_key

# ключ бота в файле settings, в github не отправляется
bot = telebot.TeleBot(api_key)


# по команде боту /boss вызывает парсер, получает словарь с именами и датами респа боссов,
# через цикл отдельными сообщениями отвечает пользователю в чат
@bot.message_handler(commands=['boss'])
def start_bot(message):
    bosses = Parser.get_bosses()
    bot.send_message(message.chat.id, f'Список эпик боссов в порядке от ближайшего:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')


bot.polling()
