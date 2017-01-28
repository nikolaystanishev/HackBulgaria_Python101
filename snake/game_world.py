from cell import Cell
from python import Python
import settings
from error import DeathError


class GameWorld:
    def __init__(self, size):
        self.size = size
        self.head_position = None
        self.position = None
        self.python_size = 0
        self.create_game()

    def create_game(self):
        self.matrix = [[Cell() for col in range(self.size)]
                       for row in range(self.size)]

    def print_game(self):
        for row in range(self.size):
            for col in range(self.size):
                print(self.matrix[row][col], end=' ')
            print()

    def get_wall(self):
        position = settings.choose_position(self.matrix, self.size)
        self.matrix[position[0]][position[1]].promote_to_wall()

    def get_black_hole(self):
        position = settings.choose_position(self.matrix, self.size)
        self.matrix[position[0]][position[1]].promote_to_black_hole()

    def get_food(self):
        position = settings.choose_position(self.matrix, self.size)
        self.matrix[position[0]][position[1]]\
            .promote_to_food(settings.generate_fruit())

    def get_python(self):
        direction = settings.generate_direction()
        size = settings.generate_size()
        position = settings.choose_position(self.matrix, self.size,
                                            direction, size)
        self.matrix[position[0][0]][position[0][1]].promote_to_head()
        self.head_position = position[1]
        self.python_size = size
        position = position[1:]
        print(position)
        for x, y in position:
            self.matrix[x][y].promote_to_body()
        self.position = position

    def move_python(self, way):
        curr_pos = self.head_position
        if way == 'w' or way == 'A':
            if self.head_position[0] - 1 < 0:
                raise DeathError('Out of range')
            self.head_position = (self.head_position[0] - 1,
                                  self.head_position[1])
        elif way == 's' or way == 'B':
            if self.head_position[0] + 1 < 0:
                raise DeathError('Out of range')
            self.head_position = (self.head_position[0] + 1,
                                  self.head_position[1])
        elif way == 'a' or way == 'D':
            if self.head_position[1] - 1 < 0:
                raise DeathError('Out of range')
            self.head_position = (self.head_position[0],
                                  self.head_position[1] - 1)
        elif way == 'd' or way == 'C':
            if self.head_position[1] + 1 < 0:
                raise DeathError('Out of range')
            self.head_position = (self.head_position[0],
                                  self.head_position[1] + 1)
        else:
            return -1
        if self.matrix[self.head_position[0]][self.head_position[1]]\
               .is_black_hole():
            raise DeathError('You hit black hole')
        if self.matrix[self.head_position[0]][self.head_position[1]]\
               .is_wall():
            raise DeathError('You hit wall')
        self.matrix[curr_pos[0]][curr_pos[1]].empty_cell()
        self.matrix[curr_pos[0]][curr_pos[1]].promote_to_body()
        self.position.insert(0, curr_pos)
        last_position = self.position.pop()
        self.matrix[last_position[0]][last_position[1]].empty_cell()
        self.matrix[self.head_position[0]][self.head_position[1]]\
            .promote_to_head()
        if self.matrix[self.head_position[0]][self.head_position[1]]\
               .is_food():
            self.matrix[self.head_position[0]][self.head_position[1]]\
                .eat_food()
            self.get_food()
            self.matrix[last_position[0]][last_position[1]].promote_to_body()
            self.position.append(last_position)

    def __getitem__(self, index):
        if index > self.size:
            raise StopIteration()
        return self.matrix[index]
