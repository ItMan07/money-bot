from loader import *


@bot.message_handler(commands=['reg', 'Регистрация'])
def cmd_reg(message):
    id = message.from_user.id

    sql.execute(f"SELECT id FROM users WHERE id = {id}")
    if sql.fetchone() is None:
        msg = bot.send_message(message.chat.id, '❇ Придумайте себе ник (<b>на английском языке</b>)', parse_mode='html')

        bot.register_next_step_handler(msg, reg2)
    else:
        bot.send_message(message.chat.id, '⛔ У вас уже есть учетная запись!', parse_mode='html')


def cmd_reg2(message):
    username = message.text
    username = username.lower()
    id = message.from_user.id

    sec = time.time()
    sec += 10800
    reg_date = time.ctime(sec)

    sql.execute(f"SELECT username FROM users WHERE username = '{username}'")
    if sql.fetchone() is None:

        sql.execute("INSERT INTO users(id, username, money, f_name, l_name, time, admin)"
                    " VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (id, username, reg_money, message.from_user.first_name, message.from_user.last_name, reg_date,
                     default_admin))

        db.commit()
        db.close()
        bot.send_message(message.chat.id, '✅ Успешно! Вы зарегистрированы! \n\n💰 Ваш начальный баланс: 5000',
                         parse_mode='html')
    else:
        bot.send_message(message.chat.id, '⛔ Данное имя пользователя уже занято! \n Попробуйте еще раз! (/reg)',
                         parse_mode='html')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)

    btn1 = types.KeyboardButton('/Перевод')
    btn2 = types.KeyboardButton('/Баланс')
    btn4 = types.KeyboardButton('/Казино')
    btn5 = types.KeyboardButton('/Помощь')
    btn6 = types.KeyboardButton('/Инфо')

    markup.add(btn1, btn2, btn6, btn4, btn5)

    bot.send_message(message.chat.id, 'Выберите действие', parse_mode='html', reply_markup=markup)
