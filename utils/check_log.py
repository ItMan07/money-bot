from loader import *


def is_log_id(id):
    sql.execute(f"SELECT id FROM users WHERE id = {id}")
    user = sql.fetchone()[0]

    if user is None:
        return False
    else:
        return True


def is_log_username(username):
    sql.execute(f"SELECT id FROM users WHERE username = '{username}'")
    user = sql.fetchone()[0]

    if user is None:
        return False
    else:
        return True
