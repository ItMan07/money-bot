from loader import *


@bot.message_handler(commands=['info', 'Инфо'])
def cmd_info(message):
    id = message.from_user.id

    sql.execute(f"SELECT username FROM users WHERE id = {id}")
    username = sql.fetchone()[0]

    sql.execute(f"SELECT money FROM users WHERE id = {id}")
    cash = sql.fetchone()[0]

    sql.execute(f"SELECT time FROM users WHERE id = {id}")
    reg_date = sql.fetchone()[0]

    bot.send_message(message.chat.id, f'❇ Ваш id: {id}\n\n📌 Ваш username: {username}'
                                      f'\n\n💰 Ваш баланс: {cash}'
                                      f'\n\n⏱️ Дата регистрации по МСК (GMT+3):\n{reg_date}', parse_mode='html')
