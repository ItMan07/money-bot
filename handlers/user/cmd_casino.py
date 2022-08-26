from loader import *


@bot.message_handler(commands=['casino', 'Казино'])
def cmd_casino(message):
    id = message.from_user.id

    sql.execute(f"SELECT id FROM users WHERE id = {id}")
    if sql.fetchone() is None:
        bot.send_message(message.chat.id, '⛔ Вы не зарегистрированы! Пройдите регистрацию!', parse_mode='html')
    else:
        sql.execute(f"SELECT money FROM users WHERE id = {id}")
        cash = sql.fetchone()[0]

        bot.send_message(message.chat.id, f"Добро пожаловать в \n<b>КАЗИНО 777</b> 🎰 🎲 🎰", parse_mode='html')
        msg = bot.send_message(message.chat.id, f"💰 Ваш баланс: {cash} \n\n💸 Сделайте ставку "
                                                f"\n\n(0 - если хотите отменить)", parse_mode='html')
        bot.register_next_step_handler(msg, cmd_casino2)


def cmd_casino2(message):
    stavka = message.text

    if stavka.isdigit():
        stavka = int(stavka)

        id = message.from_user.id
        sql.execute(f"SELECT money FROM users WHERE id = {id}")
        cash = sql.fetchone()[0]

        if stavka == 0:
            bot.send_message(message.chat.id, '👍 Вот и молодец. Азарт - плохое дело!', parse_mode='html')

        elif min_stavka <= stavka <= cash:
            bot.send_message(message.chat.id, '✅ Отлично ставка сделана! \n\n🎰 Крутим барабан...', parse_mode='html')

            if chanceGenerate():
                cash = cash + stavka * 2
                sql.execute(f"UPDATE users SET money = {cash} WHERE id = {id}")
                db.commit()
                bot.send_message(message.chat.id, f'💵 Поздравляю вы <b>выиграли! \n\n💰 Ваш баланс: {cash}</b>',
                                 parse_mode='html')
            else:
                cash = cash - stavka
                sql.execute(f"UPDATE users SET money = {cash} WHERE id = {id}")
                db.commit()
                bot.send_message(message.chat.id, f'😢 К сожалению вы <b>проиграли! \n\n💰 Ваш баланс: {cash}</b>',
                                 parse_mode='html')

        elif stavka > cash:
            bot.send_message(message.chat.id, '⛔ Вы не можете поставить сумму больше чем ваш баланс', parse_mode='html')

        elif stavka < 100:
            bot.send_message(message.chat.id, '⚠️ Минимальная сумма для игры - 100 коинов', parse_mode='html')
        else:
            bot.send_message(message.chat.id, '⚠️ Ошибка (error №404 casino)', parse_mode='html')

    else:
        bot.send_message(message.chat.id, f'⚠️ Неверный тип данных.\n Попробуйте еще раз! (/casino)')
