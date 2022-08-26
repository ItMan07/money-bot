from loader import *
from utils import is_admin, is_log_username


@bot.message_handler(commands=['edit_money'])
def cmd_edit_money(message):
    if is_admin(message.from_user.id):
        msg = bot.send_message(message.chat.id, '❇ Введите username: ', parse_mode='html')
        bot.register_next_step_handler(msg, cmd_edit_money2)
    else:
        bot.send_message(ADMIN_ID, f"⚠️  ⚠️  ⚠️ \n"
                                   f"Пользователь: {message.from_user.first_name}\n"
                                   f" id: message.from_user.id \n"
                                   f"пытался использовать команду /edit_money")


def cmd_edit_money2(message):
    global username_red
    username_red = message.text
    username_red = username_red.lower()

    if is_log_username(username_red):
        msg = bot.send_message(message.chat.id, '💸 Введите <b><u>значение</u></b>: \n\n'
                                                '(0 - если хотите отменить)', parse_mode='html')
        bot.register_next_step_handler(msg, cmd_edit_money3)
    else:
        bot.send_message(message.chat.id, '⛔ Ошибка! Пользователся с таким id не существует!', parse_mode='html')


def cmd_edit_money3(message):
    global money_red
    money_red = message.text
    if money_red.isdigit():
        money_red = int(money_red)

        if money_red == '0':
            bot.send_message(message.chat.id, '⛔ Операция отменена')
        else:
            sql.execute(f"UPDATE users SET money = {money_red} WHERE username = '{username_red}'")
            db.commit()

            bot.send_message(message.chat.id, '✅ Успешно', parse_mode='html')

    else:
        bot.send_message(message.chat.id, f'⚠ Неверный тип данных.\n Попробуйте еще раз! (/edit_money)')
