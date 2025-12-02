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
        value_list = []
        for i in roman_string:
            value_list.append(numerals[i])
        for i in range(len(value_list)-1):
            if value_list[i] < value_list[i+1]:
                value_list[i] = -value_list[i]
        return sum(value_list)
    except TypeError:
        return 0
