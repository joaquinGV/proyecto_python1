from audioop import mul
from functools import reduce


def run():
    my_list = [2, 2, 2, 2, 2]

    multiplied = (reduce(lambda x, y: x*y, my_list))
    print(multiplied)


if __name__ == '__main__':
    run()
