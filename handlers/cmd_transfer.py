from loader import *


@bot.message_handler(commands=['perevod', 'Перевод'])
def cmd_transfer(message):
    msg = bot.send_message(message.chat.id, '📥 Введите <u><b>username</b></u> получателя \n\n '
                                            '(0 - если хотите отменить)', parse_mode='html')

    bot.register_next_step_handler(msg, cmd_transfer2)


def cmd_transfer2(message):
    global recipient
    recipient = message.text
    recipient = recipient.lower()

    if recipient == '0':
        bot.send_message(message.chat.id, '⛔ Операция отменена', parse_mode='html')
    else:
        sql.execute(f"SELECT id FROM users WHERE username = '{recipient}'")
        recipient_id = sql.fetchone()[0]

        if recipient is None:
            bot.send_message(message.chat.id, '⛔ Ошибка! <b>Пользователся с таким username не существует!</b>',
                             parse_mode='html')
        else:
            sql.execute(f"SELECT id FROM users WHERE id = {message.from_user.id}")
            sender_id = sql.fetchone()[0]

            if recipient_id == sender_id:
                bot.send_message(message.chat.id, '⛔ Ошибка! Вы не можете отправить деньги самому себе',
                                 parse_mode='html')
            else:
                msg = bot.send_message(message.chat.id, '💸 Введите сумму: ', parse_mode='html')
                bot.register_next_step_handler(msg, cmd_transfer3)


def cmd_transfer3(message):
    money = message.text

    if money.isdigit():
        money = int(money)

        id = message.from_user.id

        sql.execute(f"SELECT money FROM users WHERE id = {id}")  # СКОЛЬКО ДЕНЕГ У ОТПРАВИТЕЛЯ
        cash_sender = sql.fetchone()[0]
        sql.execute(f"SELECT username FROM users WHERE id = {id}")
        sender = sql.fetchone()[0]

        sql.execute(f"SELECT money FROM users WHERE username = '{recipient}'")  # СКОЛЬКО ДЕНЕГ У ПОЛУЧАТЕЛЯ
        cash_recipient = sql.fetchone()[0]
        sql.execute(f"SELECT id FROM users WHERE username = '{recipient}'")
        recipient_id = sql.fetchone()[0]

        if money <= 0:
            bot.send_message(message.chat.id, '⛔ Ошибка! Вы не можете отправлять сумму меньше или равную нулю',
                             parse_mode='html')
        elif cash_sender >= money > 0:
            res1 = cash_sender - money
            res2 = cash_recipient + money

            sql.execute(f"UPDATE users SET money = {res1} WHERE id = {id}")
            db.commit()
            sql.execute(f"UPDATE users SET money = {res2} WHERE username = '{recipient}'")
            db.commit()
            db.close()

            sec = time.time()
            sec += 10800
            transfer_date = time.ctime(sec)

            bot.send_message(message.chat.id,
                             f'✅ Перевод совершен <b>успешно</b>\n\n💳 Сумма: {money}\n\n📥 Получатель: {recipient}'
                             f' \n\n💰 Ваш баланс: {res1} \n\n⏱️ Время: {transfer_date}', parse_mode='html')

            bot.send_message(recipient_id, f"💸 <b>Пополнение баланса!</b> \n\n💳 Сумма: {money}\n\n💰 Баланс: {res2}"
                                           f"\n\n📤 Отправитель: {sender} \n\n⏱️ Время: {transfer_date}",
                             parse_mode='html')
        elif cash_recipient < money:
            bot.send_message(message.chat.id, f'⛔ Недостаточно средств! \n <b>Платеж отклонен</b>'
                                              f' \n\n💰 Ваш баланс: {cash_sender}', parse_mode='html')
    else:
        bot.send_message(message.chat.id, f'⚠️ Неверный тип данных.\n Попробуйте еще раз! (/perevod)')
