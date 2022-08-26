from loader import *
from utils import is_admin


@bot.message_handler(commands=['admin_panel'])
def cmd_admin_panel(message):
    if is_admin(message.from_user.id):
        admin_panel = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item_start = types.KeyboardButton('/start')
        item_admins = types.KeyboardButton('/set_admin')
        item_balance = types.KeyboardButton('/edit_balance')
        item_data = types.KeyboardButton('/data')

        admin_panel.add(item_start, item_admins, item_balance, item_data)
        bot.send_message(message.chat.id, 'Админ панель:', reply_markup=admin_panel)
    else:
        bot.send_message(ADMIN_ID, f"⚠️  ⚠️  ⚠️ \n"
                                   f"Пользователь: {message.from_user.first_name}\n"
                                   f" id: message.from_user.id \n"
                                   f"пытался использовать команду /admin_panel")

