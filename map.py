def run():
    my_list = [1, 2, 3, 4, 5]

    list4 = list(map(lambda x: x*x, my_list))
    print(list4)


if __name__ == '__main__':
    run()
