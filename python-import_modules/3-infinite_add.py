#!/usr/bin/python3
import sys
if __name__ == '__main__':
    argv = sys.argv[1:]
    s = 0
    for i in argv:
        s += int(i)
    print('{}'.format(s))
