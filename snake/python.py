import settings


class Python():
    def __init__(self):
        pass

    def promote_to_head(self):
        self.content = settings.SNAKE_HEAD

    def promote_to_body(self):
        self.content = settings.SNAKE_BODY
        self.isbody = 1
