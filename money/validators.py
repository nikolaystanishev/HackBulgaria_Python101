import re


def validate_password(username, password):
    return bool(re.match('^(?=.*?\d)(?=.*?[ !"#$%&\'()*+,\-.\/:;<=>?@\[\]^_`{|'
                         '}~])(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d !"#$%&\'()*+,'
                         '\-.\/:;<=>?@\[\]^_`{|}~]{8,}$',
                         password)) and username not in password
