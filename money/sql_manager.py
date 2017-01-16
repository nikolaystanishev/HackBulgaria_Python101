import sqlite3
from client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''
        CREATE TABLE IF NOT EXISTS clients(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            email TEXT,
            balance REAL DEFAULT 0,
            message TEXT,
            reset_password_code TEXT,
            tan_code TEXT DEFAULT NULL
        )
    '''
    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = '''
        UPDATE clients
        SET message = ?
        WHERE id = ?
    '''
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = '''
        UPDATE clients
        SET password = ?
        WHERE id = ?
    '''
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password, email):
    insert_sql = '''
        INSERT INTO clients (username, password, email)
        VALUES (?, ?, ?)
    '''
    cursor.execute(insert_sql, (username, password, email))
    conn.commit()


def login(username, password):
    select_query = '''
        SELECT id, username, balance, message, email
        FROM clients
        WHERE username = ? AND password = ? LIMIT 1
    '''
    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3], user[4])
    else:
        return False


def find_user(username):
    select_query = '''
        SELECT email
        FROM clients
        WHERE username = ? LIMIT 1
    '''
    cursor.execute(select_query, (username,))
    email = cursor.fetchone()
    return email[0]


def add_code_for_reset_password(code, email):
    update_sql = '''
        UPDATE clients
        SET reset_password_code = ?
        WHERE email = ?
    '''
    cursor.execute(update_sql, (code, email))
    conn.commit()


def get_reset_code(username):
    select_query = '''
        SELECT reset_password_code
        FROM clients
        WHERE username = ?
    '''
    cursor.execute(select_query, (username,))
    code = cursor.fetchone()
    return code[0]


def change_pass_from_code(username, new_pass):
    update_sql = '''
        UPDATE clients
        SET password = ?, reset_password_code = Null
        WHERE username = ?
    '''
    cursor.execute(update_sql, (new_pass, username))
    conn.commit()


def set_ten_tan_codes(user_id, ten_tan_codes):
    update_sql = '''
        UPDATE clients
        SET tan_code = ?
        WHERE id = ?
    '''
    cursor.execute(update_sql, (ten_tan_codes, user_id))
    conn.commit()


def is_tan_code(username):
    select_query = '''
        SELECT tan_code
        FROM clients
        WHERE username = ?
    '''
    cursor.execute(select_query, (username,))
    code = cursor.fetchone()
    return code[0]


def get_tan(user_id):
    select_query = '''
        SELECT tan_code
        FROM clients
        WHERE id = ?
    '''
    cursor.execute(select_query, (user_id,))
    codes = cursor.fetchone()
    return codes[0]


def deposit(amount, user_id):
    update_sql = '''
        UPDATE clients
        SET balance = ?
        WHERE id = ?
    '''
    cursor.execute(update_sql, (amount, user_id))
    conn.commit()


def withdraw(amount, user_id):
    update_sql = '''
        UPDATE clients
        SET balance = ?
        WHERE id = ?
    '''
    cursor.execute(update_sql, (amount, user_id))
    conn.commit()


def get_balance(user_id):
    select_query = '''
        SELECT balance
        FROM clients
        WHERE id = ?
    '''
    cursor.execute(select_query, (user_id,))
    codes = cursor.fetchone()
    return codes[0]
