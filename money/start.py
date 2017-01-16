import sql_manager
import validators
import smtpinfo
from getpass import getpass
import hashlib
import smtplib
import os
import binascii
import time
import json


def main_menu():
    print("Welcome to our bank service. You are not logged in.\
           \nPlease register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            email = input("Enter your email: ")
            if validators.validate_password(username, password):
                hash_pass = hashlib.sha256(password.encode()).hexdigest()
                sql_manager.register(username, hash_pass, email)

                print("Registration Successfull")
            else:
                print('Your password must have a more then 8 symbols, capital'
                      ' letters, and numbers and a special symbol '
                      'Username is not in the password (as a substring)')

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            hash_pass = hashlib.sha256(password.encode()).hexdigest()
            logged_user = sql_manager.login(username, hash_pass)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command.find("send-reset-password") >= 0:
            email = sql_manager.find_user(' '.join(command.split()[1:]))
            code_and_email = send_email(email)
            sql_manager.add_code_for_reset_password(code_and_email[0],
                                                    code_and_email[1])

        elif command.find("reset-password") >= 0:
            reset_password(' '.join(command.split()[1:]))

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")
            print("send-reset-password - for send code for reset")
            print("reset-password - for reset password")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass("Enter your new password: ")

            if validators.validate_password(logged_user.get_username(),
                                            new_pass):
                hash_pass = hashlib.sha256(new_pass.encode()).hexdigest()
                sql_manager.change_pass(hash_pass, logged_user)
            else:
                print('Your password must have a more then 8 symbols, capital'
                      ' letters, and numbers and a special symbol '
                      'Username is not in the password (as a substring)')

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'deposit':
            amount = input("Enter amount: ")
            tan_code = input("Enter TAN code: ")
            tan_codes = sql_manager.get_tan(logged_user.get_id())
            if tan_codes:
                tan_codes_list = tan_codes.replace('[', '')\
                                          .replace('\'', '')\
                                          .replace('"', '')\
                                          .replace(']', '')\
                                          .replace(',', ' ').split()
                if tan_code in tan_codes_list:
                    tan_codes_list.remove(tan_code)
                    sql_manager.set_ten_tan_codes(logged_user.get_id(),
                                                  json.dumps(tan_codes_list))
                    sql_manager.deposit(amount, logged_user.get_id())
                    print("Transaction successful!\n"
                          "{} were deposited to the bank".format(amount))
                    continue
            print("Transaction unsuccessful!")

        elif command == 'withdraw':
            amount = input("Enter amount: ")
            tan_code = input("Enter TAN code: ")
            tan_codes = sql_manager.get_tan(logged_user.get_id())
            if tan_codes:
                tan_codes_list = tan_codes.replace('[', '')\
                                          .replace('\'', '')\
                                          .replace('"', '')\
                                          .replace(']', '')\
                                          .replace(',', ' ').split()
                if tan_code in tan_codes_list:
                    tan_codes_list.remove(tan_code)
                    sql_manager.set_ten_tan_codes(logged_user.get_id(),
                                                  json.dumps(tan_codes_list))
                    balance = sql_manager.get_balance(logged_user.get_id())
                    if balance >= float(amount):
                        sql_manager.withdraw((balance - float(amount)),
                                             logged_user.get_id())
                        print("Transaction successful!\n"
                              "{} were withdraw from the bank".format(amount))
                        continue
            print("Transaction unsuccessful!")

        elif command == 'balance':
            balance = sql_manager.get_balance(logged_user.get_id())
            print(balance)

        elif command == 'get-tan':
            password = getpass("Enter your password: ")
            hash_pass = hashlib.sha256(password.encode()).hexdigest()
            logged_user = sql_manager.login(logged_user.get_username(),
                                            hash_pass)

            if logged_user:
                tan_codes = sql_manager.get_tan(logged_user.get_id())
                if tan_codes:
                    tan_codes_list = tan_codes.replace('[', '')\
                                              .replace('\'', '')\
                                              .replace('"', '')\
                                              .replace(']', '')\
                                              .replace(',', ' ').split()
                    print("You have {0} remaining TAN codes to use"
                          .format(len(tan_codes_list)))
                else:
                    ten_tan_codes = [binascii.hexlify(os.urandom(16))
                                             .decode('utf8')
                                     for _ in range(10)]
                    sql_manager.set_ten_tan_codes(logged_user.get_id(),
                                                  json.dumps(ten_tan_codes))
                    send_email_with_tan(ten_tan_codes, logged_user.get_email())
            else:
                print("Login failed")
                break

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("get-tan - for gettin tan codes")
            print("deposit - for deposit")
            print("balance - Display the current balance"
                  "from the bank account")
            print("withdraw - Withdraw money from the bank account")


def reset_password(username):
    code = input('Enter your reset code: ')
    if code == sql_manager.get_reset_code(username):
        new_pass = getpass("Enter your new password: ")
        if validators.validate_password(username, new_pass):
            hash_pass = hashlib.sha256(new_pass.encode()).hexdigest()
            sql_manager.change_pass_from_code(username, hash_pass)
        else:
            print('Your password must have a more then 8 symbols, capital'
                  ' letters, and numbers and a special symbol '
                  'Username is not in the password (as a substring)')
    else:
        print('Your code is wrong')


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


def main():
    sql_manager.create_clients_table()
    main_menu()


if __name__ == '__main__':
    main()
