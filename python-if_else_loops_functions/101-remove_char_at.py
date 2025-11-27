#!/usr/bin/python3

def remove_chart_at(str, n):
    str = list(str)
    str[n] = ''
    return ''.join(str)
