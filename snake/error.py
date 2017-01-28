class Error(Exception):
    def __init__(self):
        pass


class DeathError(Error):
    def __init__(self, msg):
        self.msg = msg

    def get_msg(self):
        return self.msg
