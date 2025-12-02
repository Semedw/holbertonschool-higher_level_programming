#!/usr/bin/python3

def divisible_by_2(mylist):
    result = []
    for i in mylist:
        if i % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
