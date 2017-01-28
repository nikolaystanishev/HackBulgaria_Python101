from wall import Wall
from black_hole import BlackHole
from food import Food
from python import Python
import settings


class Cell(Wall, BlackHole, Food, Python):
    def __init__(self, content=settings.EMPTY_CELL):
        self.content = content
        self.position = ()
        self.isbody = 0
        self.iswall = 0
        self.isblackhole = 0
        self.isfood = 0

    def is_empty(self):
        return True if self.position == () else False

    def is_body(self):
        return bool(self.isbody)

    def is_wall(self):
        return bool(self.iswall)

    def is_black_hole(self):
        return bool(self.isblackhole)

    def is_food(self):
        return bool(self.isfood)

    def eat_food(self):
        self.isfood = 0

    def empty_cell(self):
        self.content = settings.EMPTY_CELL
        self.isbody = 0
        self.iswall = 0
        self.isblackhole = 0
        self.isfood = 0

    def get_position(self):
        return self.position

    def __str__(self):
        return self.content
