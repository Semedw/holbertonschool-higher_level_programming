#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i, 10):
        if i != j:
            print("{}{}".format(str(i), str(j)), end=', ') if str(i) + str(j) != '89' else print("{}".format(89))
