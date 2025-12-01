#!/usr/bin/python3
def add_tuple(a, b):
    tuple1 = []
    tuple1.append(list(a)[0]+list(b)[0])
    tuple1.append(list(b)[1]+list(a)[1])
    tuple1 = tuple(tuple1)
    return tuple1
