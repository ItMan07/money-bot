from loader import *
from utils import is_admin


@bot.message_handler(commands=['edit'])
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

    msg = bot.send_message(message.chat.id, '💸 Введите сумму: ', parse_mode='html')
    bot.register_next_step_handler(msg, cmd_edit_money3)


def cmd_edit_money3(message):
    global money_red
    money_red = message.text
    if money_red.isdigit():

        money_red = int(money_red)
        sql.execute(f"UPDATE users SET money = {money_red} WHERE username = '{username_red}'")
        db.commit()

        bot.send_message(message.chat.id, '✅ Успешно', parse_mode='html')

    else:
        bot.send_message(message.chat.id, f'⚠️ Неверный тип данных.\n Попробуйте еще раз! (/edit)')
