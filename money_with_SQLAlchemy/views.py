import controlers
from error import InvalidPass, WrongUser, TransactionError

from getpass import getpass

from sqlalchemy.orm.exc import NoResultFound


def main_menu():
    print('Welcome to our bank service. You are not logged in.\n'
          'Please register or login')
    while True:
        command = input('$$$> ')
        if command == 'register':
            username = input('Enter your username: ')
            password = getpass('Enter your password: ')
            email = input('Enter your email: ')
            try:
                controlers.register(username, password, email)
                print('Registration Successfull')
            except InvalidPass as e:
                print(e)
        elif command == 'login':
            username = input('Enter your username: ')
            password = getpass('Enter your password: ')
            try:
                user = controlers.login(username, password)
                logged_menu(user)
            except NoResultFound as e:
                print('Wrong username or password')
        elif command.find('send-reset-password') >= 0:
            try:
                controlers.genetate_reset_code(' '.join(command.split()[1:]))
            except NoResultFound as e:
                print('Wrong username or password')
        elif command.find('reset-password') >= 0:
            try:
                code = input('Enter your reset code: ')
                if code == controlers.get_reset_code(' '.join(command
                                                              .split()[1:])):
                    new_pass = getpass('Enter your new password: ')
                    controlers.reset_password(' '.join(command.split()[1:]),
                                              new_pass)
                else:
                    raise WrongUser('Your code is wrong')
            except WrongUser as e:
                print(e)
            except InvalidPass as e:
                print(e)
            except NoResultFound as e:
                print('Wrong username or password')
        elif command == 'help':
            print('login - for logging in!')
            print('register - for creating new account!')
            print('exit - for closing program!')
            print('send-reset-password - for send code for reset')
            print('reset-password - for reset password')
        elif command == 'exit':
            break
        else:
            print('Not a valid command')


def logged_menu(user):
    print('Welcome you are logged in as: ' + user.username)
    while True:
        command = input('Logged>> ')
        if command == 'info':
            print('You are: ' + user.username)
            print('Your id is: ' + str(user.id))
            print('Your balance is: ' + str(user.balance))
        elif command == 'changepass':
            new_pass = getpass('Enter your new password: ')
            try:
                controlers.reset_password(user.username, new_pass)
            except InvalidPass as e:
                print(e)
        elif command == 'change-message':
            new_message = input('Enter your new message: ')
            controlers.change_message(user.username, new_message)
        elif command == 'show-message':
            print(user.message)
        elif command == 'deposit':
            amount = input('Enter amount: ')
            tan_code = input('Enter TAN code: ')
            try:
                controlers.deposit(amount, tan_code, user)
                print('Transaction successful!\n'
                      '{} were deposited to the bank'.format(amount))
            except TransactionError as e:
                print(e)
        elif command == 'withdraw':
            amount = input('Enter amount: ')
            tan_code = input('Enter TAN code: ')
            try:
                controlers.withdraw(amount, tan_code, user)
                print('Transaction successful!\n'
                      '{} were withdraw from the bank'.format(amount))
            except TransactionError as e:
                print(e)
        elif command == 'balance':
            print(user.balance)
        elif command == 'get-tan':
            password = getpass('Enter your password: ')
            try:
                num_of_tan = controlers.get_tan(user, password)
                if num_of_tan:
                    print("You have {0} remaining TAN codes to use"
                          .format(num_of_tan))
            except TransactionError as e:
                print(e)
            except WrongUser as e:
                print(e)
        elif command == 'exit':
            break
        elif command == 'help':
            print('info - for showing account info')
            print('changepass - for changing passowrd')
            print('change-message - for changing users message')
            print('show-message - for showing users message')
            print('get-tan - for gettin tan codes')
            print('deposit - for deposit')
            print('balance - Display the current balance'
                  'from the bank account')
            print('withdraw - Withdraw money from the bank account')
            print('exit - for exit from account!')
        else:
            print('Not a valid command')


def main():
    main_menu()


if __name__ == '__main__':
    main()
