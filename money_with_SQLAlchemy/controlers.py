from models import Clients
from validators import validate_password
from error import InvalidPass, WrongUser, TransactionError
from settings import DB_NAME
import smtpinfo

import hashlib
import smtplib
import time
import binascii
import os
import json

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(DB_NAME)
Session = sessionmaker(bind=engine)
session = Session()


def register(username, password, email):
    if validate_password(username, password):
        hash_pass = hashlib.sha256(password.encode()).hexdigest()
        client = Clients(username=username, password=hash_pass, email=email)
        session.add(client)
        session.commit()
    else:
        raise InvalidPass('Your password must have a more then 8 symbols,'
                          'capital letters, and numbers and a special symbol '
                          'Username is not in the password (as a substring)')


def login(username, password):
    hash_pass = hashlib.sha256(password.encode()).hexdigest()
    user = session.query(Clients).filter(Clients.username == username,
                                         Clients.password == hash_pass).one()

    if user:
        return user
    else:
        raise WrongUser('Wrong username or password')


def get_email(username):
    user = session.query(Clients).filter(Clients.username == username).one()

    if user:
        return user.email
    else:
        raise WrongUser('Wrong user')


def add_code_for_reset_password(code, email):
    user = session.query(Clients).filter(Clients.email == email).one()
    user.reset_code = code
    session.commit()


def send_email(email):
    fromMy = smtpinfo.username
    to = email
    subj = 'Confirm'
    date = time.strftime("%d/%m/%Y")
    code = binascii.hexlify(os.urandom(16)).decode('utf8')
    msg_text = 'Your reset code is: ' + code

    msg = "From: {0}\nTo: {1}\nSubject: {2}\nDate: {3}\n\n{4}".format(fromMy,
                                                                      to, subj,
                                                                      date,
                                                                      msg_text)

    username = smtpinfo.username
    password = smtpinfo.password

    try:
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(fromMy, to, msg)
        server.quit()
        print('The email has sent!')
        return (code, email)
    except:
        print('Can\'t send the email!')


def genetate_reset_code(username):
    email = get_email(username)
    code_and_email = send_email(email)
    add_code_for_reset_password(code_and_email[0],
                                code_and_email[1])


def get_reset_code(username):
    user = session.query(Clients).filter(Clients.username == username).one()

    if user:
        return user.reset_code
    else:
        raise WrongUser('Wrong user')


def change_pass_from_code(username, password):
    user = session.query(Clients).filter(Clients.username == username).one()
    user.password = password
    user.reset_code = None
    session.commit()


def reset_password(username, new_pass):
    if validate_password(username, new_pass):
        hash_pass = hashlib.sha256(new_pass.encode()).hexdigest()
        change_pass_from_code(username, hash_pass)
    else:
        raise InvalidPass('Your password must have a more then 8 symbols,'
                          'capital letters, and numbers and a special '
                          'symbol Username is not in the password (as a'
                          ' substring)')


def change_message(username, new_msg):
    user = session.query(Clients).filter(Clients.username == username).one()
    user.message = new_msg
    session.commit()


def deposit(amount, tan_code, user):
    tan_codes = user.tan_code
    if tan_codes:
        tan_codes_list = tan_codes.replace('[', '')\
                                  .replace('\'', '')\
                                  .replace('"', '')\
                                  .replace(']', '')\
                                  .replace(',', ' ').split()
        if tan_code in tan_codes_list:
            tan_codes_list.remove(tan_code)
            user.tan_code = json.dumps(tan_codes_list)
            user.balance += float(amount)
            session.commit()
            return
    raise TransactionError("Transaction unsuccessful!")


def withdraw(amount, tan_code, user):
    tan_codes = user.tan_code
    if tan_codes:
        tan_codes_list = tan_codes.replace('[', '')\
                                  .replace('\'', '')\
                                  .replace('"', '')\
                                  .replace(']', '')\
                                  .replace(',', ' ').split()
        if tan_code in tan_codes_list:
            tan_codes_list.remove(tan_code)
            user.tan_code = json.dumps(tan_codes_list)
            if user.balance >= float(amount):
                user.balance -= float(amount)
                session.commit()
                return
    raise TransactionError("Transaction unsuccessful!")


def send_email_with_tan(ten_tan_codes, email):
    fromMy = smtpinfo.username
    to = email
    subj = 'Tan codes'
    date = time.strftime("%d/%m/%Y")
    codes = '\n'.join(ten_tan_codes)
    msg_text = 'Your tan codes are: ' + codes

    msg = "From: {0}\nTo: {1}\nSubject: {2}\nDate: {3}\n\n{4}".format(fromMy,
                                                                      to, subj,
                                                                      date,
                                                                      msg_text)

    username = smtpinfo.username
    password = smtpinfo.password

    try:
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(fromMy, to, msg)
        server.quit()
        print('The email has sent!')
    except:
        print('Can\'t send the email!')


def get_tan(user, password):
    hash_pass = hashlib.sha256(password.encode()).hexdigest()
    if user.password == hash_pass:
        tan_codes = user.tan_code
        if tan_codes:
            tan_codes_list = tan_codes.replace('[', '')\
                                      .replace('\'', '')\
                                      .replace('"', '')\
                                      .replace(']', '')\
                                      .replace(',', ' ').split()
            return len(tan_codes_list)
        else:
            ten_tan_codes = [binascii.hexlify(os.urandom(16)).decode('utf8')
                             for _ in range(10)]
            user.tan_code = json.dumps(ten_tan_codes)
            send_email_with_tan(ten_tan_codes, user.email)
            return None
    raise WrongUser('Login failed')
