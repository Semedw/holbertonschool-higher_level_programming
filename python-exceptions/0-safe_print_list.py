#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end='')
        return x
    except IndexError:
        x = len(my_list)
        for i in range(x):
            print(i, end='')
        return x

