#!/usr/bin/python3
if __name__ == '__main__':
    print("{} arguments".format(len(argv)))
    if len(argv) > 0:
        for i in range(1, len(argv)+1):
            print("{}: {}".format(i, argv[i]))