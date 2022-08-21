from loader import *
from utils import is_admin


@bot.message_handler(commands=['set_admin'])
def cmd_set_admin(message):
    if is_admin(message.from_user.id):
        msg = bot.send_message(message.chat.id, '❇ Введите username: ', parse_mode='html')
        bot.register_next_step_handler(msg, set_admin2)
    else:
        bot.send_message(ADMIN_ID, f"⚠️  ⚠️  ⚠️ \n"
                                   f"Пользователь: {message.from_user.first_name}\n"
                                   f" id: message.from_user.id \n"
                                   f"пытался использовать команду /set_admin")


def set_admin2(message):
    global username_red
    username_red = message.text

    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='✅', callback_data='1')
    item_no = types.InlineKeyboardButton(text='❌', callback_data='0')

    markup_inline.add(item_yes, item_no)
    bot.send_message(message.chat.id, 'Подтвердите операцию:', reply_markup=markup_inline)


@bot.callback_query_handler(func=lambda call: True)
def set_admin3(call):
    if call.data == '1':
        sql.execute(f"SELECT username FROM users WHERE username = '{username_red}'")
        if sql.fetchone()[0] is None:
            bot.send_message(call.message.chat.id, '⛔ Такого пользователя не существует')
        else:
            sql.execute(f"UPDATE users SET admin = {True} WHERE username = '{username_red}'")
            db.commit()
            bot.send_message(call.message.chat.id, '✅ Успешно', parse_mode='html')

    elif call.data == '0':
        bot.send_message(call.message.chat.id, '⛔ Операция отменена')
