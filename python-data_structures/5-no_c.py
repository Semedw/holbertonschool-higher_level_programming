#!/usr/bin/python3
def no_c(mystring):
    mystring = list(mystring)
    for i in range(len(mystring)):
        if mystring[i] == 'c' or mystring == 'C':
            mystring[i] == ''
    return ''.join(mystring)
