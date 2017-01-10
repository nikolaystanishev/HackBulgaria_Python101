import sqlite3
from settings.sql_creation_settings import DB_NAME
import queries.manage_db_queries as queries


class Users:
    def __init__(self):
        self.db = sqlite3.connect(DB_NAME)
        self.db.row_factory = sqlite3.Row
        self.c = self.db.cursor()

    def is_user(self, user_and_pass):
        is_user = queries.IS_USER_IN_USERS
        result = self.c.execute(is_user, (user_and_pass[0], user_and_pass[1]))
        first = result.fetchone()
        if first is not None:
            return first
        else:
            return None

    def is_username(self, username):
        is_username = queries.IS_USER_IN_USERS
        result = self.c.execute(is_username, (username, '%%'))
        first = result.fetchone()
        if first is not None:
            return True
        else:
            return False

    def registration(self, user_and_pass):
        insert_user = queries.INSERT_INTO_USERS_TABLE
        self.c.execute(insert_user, (user_and_pass[0], user_and_pass[1]))
        self.db.commit()
        return self.is_user(user_and_pass)
