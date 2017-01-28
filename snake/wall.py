import settings


class Wall:
    def __init__(self):
        pass

    def promote_to_wall(self):
        self.content = settings.WALL_CELL
        self.iswall = 1
