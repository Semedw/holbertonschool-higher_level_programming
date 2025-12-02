#!/usr/bin/python3
numerals = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

def roman_to_int(roman_string):
    try:
        s = 0
        l = []
        for i in roman_string:
            l.append(numerals[i])
        for i in range(len(l)-1):
            if l[i] < l[i+1]:
                l[i] = -l[i]
        return sum(l)
    except TypeError:
        return None
