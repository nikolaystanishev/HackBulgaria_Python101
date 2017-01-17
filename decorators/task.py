import time
import datetime


def accepts(name, *args):
    def acceptss(func):
        def decorated(name, *args):
            if not isinstance(name, str):
                raise TypeError
            return func(name, *args)
        return decorated
    return acceptss


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)

# print(say_hello("dssdsd"))
# print(say_hello(218281))


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True

# print(deposit("RadoRado", 10))


def encode(string, level):
    result = ''
    for el in string:
        if el.isalpha():
            c = (ord(el) + level) % 126
            if c < 32:
                c += 31
            result += chr(c)
        else:
            result += el
    return result


def encrypt(level):
    def encryptt(func):
        def decorated():
            result = ''
            string = func()
            result = encode(string, level)
            return result
        return decorated
    return encryptt


def log(filename):
    def logg(func):
        def decorated():
            with open(filename, 'a') as log_file:
                log_file.writelines('get_low was called at ' +
                                    str(datetime.datetime.now()) + '\n')
                return func()
        return decorated
    return logg


@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"


# print(get_low())


def performance(filename):
    def performancee(func):
        def decorated():
            before = datetime.datetime.now()
            func()
            after = datetime.datetime.now()
            timedelta = after - before
            with open(filename, 'a') as log_file:
                log_file.writelines('something_heavy was called and took ' +
                                    str(timedelta) + ' to complete\n')
            return func()
        return decorated
    return performancee


@performance('log.txt')
def something_heavy():
    time.sleep(2.5)
    return "I am done!"


# print(something_heavy())
