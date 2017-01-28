class Error(Exception):
    def __init__(self):
        pass


class InvalidPass(Error):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class WrongUser(Error):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class TransactionError(Error):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
