import random

EMPTY_CELL = '□'
WALL_CELL = '■'
SNAKE_HEAD = '☭'
SNAKE_BODY = '●'

FRUITS = {
    'Banana': '🍌',
    'Strawberry': '🍓',
    'Apple': '🍎',
    'Cherries': '🍒'
}

fruits = ['Banana', 'Strawberry', 'Apple', 'Cherries']
energy = [1, 2, 3, 4, 5]


def choose_position(matrix, size, direction=(1, 1), num=1):
    if num >= 2:
        num += 1
    while True:
        positions = []
        temp_position = generate_position(size)
        for i in range(num):
            if (temp_position[0] >= 0 and
                temp_position[0] >= 0 and
                temp_position[0] <= (size - 1) and
                temp_position[0] <= (size - 1)) and\
               (temp_position[1] >= 0 and
                temp_position[1] >= 0 and
                temp_position[1] <= (size - 1) and
                temp_position[1] <= (size - 1)):
                for row in matrix:
                    for col in row:
                        if col.get_position() == temp_position:
                            break
                        else:
                            if num == 1:
                                return temp_position
                            if num - 1 == i:
                                return positions
                positions.append(temp_position)
                temp_position = (temp_position[0] + direction[0],
                                 temp_position[1] + direction[1])
            else:
                break


def generate_fruit():
    return (fruits[random.randint(0, len(fruits) - 1)],
            energy[random.randint(0, len(energy) - 1)])


def generate_position(size):
    return (random.randint(0, size - 1), random.randint(0, size - 1))


def generate_direction():
    x = 1
    y = 1
    if random.randint(0, 1):
        x = 0
        while not y:
            y = random.randint(-1, 1)
    else:
        while not x:
            x = random.randint(-1, 1)
        y = 0
    return (x, y)


def generate_size():
    return random.randint(2, 3)
