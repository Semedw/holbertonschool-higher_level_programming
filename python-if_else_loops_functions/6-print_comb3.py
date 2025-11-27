#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i, 10):
        if i != j:
            if str(i) + str(j) != '89':
                print("{}{}".format(str(i), str(j)), end=', ')
            else:
                print("{}".format(89))
