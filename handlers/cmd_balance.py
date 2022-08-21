from loader import *


@bot.message_handler(commands=['balance', 'Баланс'])
def cmd_balance(message):
    id = message.from_user.id

    sql.execute(f"SELECT id FROM users WHERE id = {id}")
    if sql.fetchone() is None:
        bot.send_message(message.chat.id, '⛔ Вы не зарегистрированы! Пройдите регистрацию!', parse_mode='html')
    else:
        sql.execute(f"SELECT money FROM users WHERE id = {id}")
        cash = sql.fetchone()[0]

        bot.send_message(message.chat.id, f"💰 Ваш баланс: {cash}", parse_mode='html')
