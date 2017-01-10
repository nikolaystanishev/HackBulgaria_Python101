import user_interface.validators as validators
import settings.general_settings as settings
from prettytable import PrettyTable
from getpass import getpass
import hashlib
import numpy
from ast import literal_eval


def input_command():
    return input('> ')


def create_database():
    return input('Do you want to create new database?(y, n)')


def insert_first_values():
    return input('Do you want to insert into database first values?(y, n)')


def show_movies(result):
    t = PrettyTable(settings.movie_col)
    for row in result:
        t.add_row([row[0], row[1], row[2]])
    print(t)


def show_projections(result):
    t = PrettyTable(settings.projection_col)
    for row in result:
        t.add_row([row[0], row[1], row[2], row[3], row[4], (100 - row[5])])
    print(t)


def registration_or_login():
    return input('Do you have account?(y, n)')
    print('You need to be a user in the system to make reservations!')


def login():
    username = input('Username: ')
    password = getpass('Password: ')
    hash_pass = hashlib.sha512(password.encode()).hexdigest()
    return (username, hash_pass)


def registration():
    username = input('Username: ')
    password = getpass('Password: ')
    if getpass('Repeat Password: ') != password:
        print('Two passwords doesn\'t match')
        if getpass('Try again: ') != password:
            print('Two passwords doesn\'t match')
            return 0
    if validators.validate_password(password):
        hash_pass = hashlib.sha512(password.encode()).hexdigest()
        return (username, hash_pass)
    else:
        print('Your password is invalid')
        return 0


def wrong_user_or_pass():
    print('Your username or password is incorrect')


def print_name(user):
    print('Hello, ' + user[1])


def username_not_free():
    print('Username is not free')


def choose_number_of_tickets():
    return input('Choose number of tickets> ')


def choose_movie():
    return input('Choose a movie> ')


def choose_projection():
    return input('Choose a projection> ')


def show_seats(seats):
    b = numpy.array(list(range(1, settings.number_of_rows + 1)))
    print(str(b).replace(',', '').replace('[', '').replace(']', '')
                .replace('  ', ' '))
    a = numpy.array(seats)
    a = numpy.c_[a, [[i] for i in range(1, settings.number_of_cols + 1)]]
    print(' ' + str(a).replace(',', '').replace('\'', '')
                      .replace('[', '').replace(']', ''))


def choose_seat(number_of_seat):
    return literal_eval(input('Choose seat {0} (row, col)> '
                        .format(number_of_seat)))


def taken_seat():
    print('This seat is taken!')


def out_of_range():
    print('Lol...NO!')


def help():
    for el in settings.options:
        print(el)


def incorrect_option():
    print('Incorrect option!')
