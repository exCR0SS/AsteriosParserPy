import telebot
import Parser
from settings import api_key

bot = telebot.TeleBot(api_key)


@bot.message_handler(commands=['boss'])
def start_bot(message):
    bosses = Parser.get_bosses()
    bot.send_message(message.chat.id, f'Список эпик боссов в порядке от ближайшего:')
    for key, value in sorted(bosses.items(), key=lambda date: (date[1], date[0])):
        bot.send_message(message.chat.id, f'{key}: {value}')


bot.polling()
