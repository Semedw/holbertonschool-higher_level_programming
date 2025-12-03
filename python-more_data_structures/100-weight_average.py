#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    s = []
    weights = []
    for i in my_list:
        number = i[0] * i[1]
        s.append(number)
        weights.append(i[1])
    return sum(s) / sum(weights)
