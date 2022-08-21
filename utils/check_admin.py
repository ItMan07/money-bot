from loader import *


def is_admin(id):
    sql.execute(f"SELECT admin FROM users WHERE id = {id}")
    return sql.fetchone()[0]
