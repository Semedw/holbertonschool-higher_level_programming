#!/usr/bin/python3
def add_tuple(a, b):
    a = list(a)
    b = list(b)
    if len(a) < 2:
        if len(a) == 1:
            a.append(0)
        else:
            a.append(0)
            a.append(0)
    if len(b) < 2:
        if len(b) == 1:
            b.append(0)
        else:
            b.append(0)
            b.append(0)
    new_list = []
    for i in range(2):
        new_list.append(a[i] + b[i])

    return tuple(new_list)
    