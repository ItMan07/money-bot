from loader import *
from utils import is_admin


@bot.message_handler(commands=['data'])
def cmd_get_data(message):
    if is_admin(message.from_user.id):
        sql.execute("SELECT * FROM users")
        reply_message = "Date base: \n\n"
        for i, item in enumerate(sql.fetchall()):
            reply_message += f"{i + 1}. {item[1].strip()} - ({item[0]}) - {item[2]} - {item[3]} - {item[4]} - {item[5]}- {item[6]}\n\n"
        bot.send_message(message.chat.id,reply_message)
