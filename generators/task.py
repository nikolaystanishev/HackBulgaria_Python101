import os
import random
import string
from Xlib import display


def chain(iterable_one, iterable_two):
    for el in iterable_one:
        yield el
    for el1 in iterable_two:
        yield el1


def compress(iterable, mask):
    for i in range(len(mask)):
        if mask[i]:
            yield iterable[i]


def cycle(iterable):
    while True:
        for el in iterable:
            yield el


def book_read(path):
    for _, _, filenames in os.walk(path):
        for file in sorted(filenames):
            with open(path + '/' + file, "r") as chapter:
                line = chapter.readline()
                while line:
                    if line[0] == '#':
                        input('')
                    yield line
                    line = chapter.readline()
            chapter.close()


def book_generate(count, lenth):
    for i in range(count):
        yield '\n# Chapter {}\n'.format(i + 1)
        for _ in range(lenth):
            yield ''.join(random.choice(string.ascii_letters)
                          for i in range(random.randint(0, 50))) + ' '


def mouse_beep():
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]


def main():
    # print(list(chain(range(0, 4), range(4, 8))))
    # print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
    # endless = cycle(range(0, 10))
    # for item in endless:
    #     print(item)
    # book = book_read("Book")
    # for el in book:
    #     print(el)
    # book = book_generate(10, 1000)
    # with open('Book1/001.txt', 'w') as file:
    #     for el in book:
    #         file.write(el)
    # book = book_read("Book1")
    # for el in book:
    #     print(el)
    while True:
        coord = mouse_beep()
        if coord == (0, 0):
            os.system('say "beep"')


if __name__ == '__main__':
    main()
