from loader import *


@bot.message_handler(commands=['help', 'Помощь'])
def cmd_help(message):
    bot.send_message(message.chat.id, '/start - Начало \n/help - Помощь \n/balance - Узнать ваш баланс'
                                      '\n/info - Узнать информацию о вас \n/reg - Зарегистрироваться'
                                      '\n/casino - Казино\n/perevod - Перевести деньги', parse_mode='html')
