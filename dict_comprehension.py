from math import sqrt


def run():
    my_dict = {i: sqrt(i) for i in range(1, 1001) if i % 3 != 0}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         my_dict[i] = i**3

    # [my_dict[i]= i**2 for i in range(1,101)]
    print(my_dict)


if __name__ == '__main__':
    run()
