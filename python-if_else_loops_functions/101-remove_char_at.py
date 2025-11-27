#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        return str
    if n > len(str):
        return str
    str = list(str)
    str[n] = ''
    return ''.join(str)
