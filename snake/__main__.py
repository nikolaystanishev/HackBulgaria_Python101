import os
import random
import getch

from game_world import GameWorld


def play():
    os.system('clear')
    size = int(input('Enter size for game: '))
    game = GameWorld(size)
    for _ in range(random.randint(5, 10)):
        game.get_wall()
    for _ in range(random.randint(2, 5)):
        game.get_black_hole()
    game.get_python()
    game.get_food()
    try:
        while True:
            os.system('clear')
            game.print_game()
            way = getch.getch()
            game.move_python(way)
    except Exception as e:
        print(e.get_msg())
    else:
        pass
    finally:
        pass


def main():
    play()


if __name__ == '__main__':
    main()
