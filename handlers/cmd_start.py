from loader import *


@bot.message_handler(commands=['start', 'Старт'])
def cmd_start(message):
    id = message.from_user.id
    sql.execute(f"SELECT * FROM users WHERE id = {id}")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    if sql.fetchone() is None:
        btn_reg = types.KeyboardButton('/Регистрация')
        markup.add(btn_reg)
        bot.send_message(message.chat.id, 'Здравствуйте 👋!\n\nКак вижу вы здесь впервые '
                                          'поэтому вам нужно пройти <b>регистрацию</b>',
                         parse_mode='html', reply_markup=markup)
    else:
        sql.execute(f"SELECT admin FROM users WHERE id = {id}")
        btn1 = types.KeyboardButton('/Перевод')
        btn2 = types.KeyboardButton('/Баланс')
        btn3 = types.KeyboardButton('/Инфо')
        btn4 = types.KeyboardButton('/Казино')
        btn5 = types.KeyboardButton('/Помощь')
        btn6 = types.KeyboardButton('/edit')
        btn7 = types.KeyboardButton('/data')

        if sql.fetchone()[0]:
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        elif not sql.fetchone()[0]:
            markup.add(btn1, btn2, btn3, btn4, btn5)

        bot.send_message(message.chat.id, 'Выберите действие', parse_mode='html', reply_markup=markup)
