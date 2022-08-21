from loader import *
from utils import is_admin


@bot.message_handler(commands=['admin_panel'])
def cmd_admin_panel(message):
    if is_admin(message.from_user.id):
        admin_panel = types.InlineKeyboardMarkup()
        item_admins = types.InlineKeyboardButton(text='Ред админов', callback_data='Ред админов')
        item_balance = types.InlineKeyboardButton(text='Ред баланс', callback_data='Ред баланс')
        item_data = types.InlineKeyboardButton(text='Просмотреть БД', callback_data='Просмотреть БД')

        admin_panel.add(item_admins, item_balance, item_data)

        bot.send_message(message.chat.id, 'Админ панель:', reply_markup=admin_panel)
    else:
        bot.send_message(ADMIN_ID, f"⚠️  ⚠️  ⚠️ \n"
                                   f"Пользователь: {message.from_user.first_name}\n"
                                   f" id: message.from_user.id \n"
                                   f"пытался использовать команду /admin_panel")


@bot.callback_query_handler(func=lambda call: True)
def cmd_admin_panel2(call):
    if call.data == 'Ред админов':
        pass

    elif call.data == 'Ред баланс':
        pass

    elif call.data == 'Просмотреть БД':
        pass

    else:
        bot.send_message(call.message.chat.id, '⚠ Неверный тип данных')
