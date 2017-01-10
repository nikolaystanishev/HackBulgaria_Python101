import re


def validate_password(password):
    return bool(re.match('^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{7,}$',
                         password))
