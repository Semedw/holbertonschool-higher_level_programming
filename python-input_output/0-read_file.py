#!/usr/bin/python3
"""
reading a text file
"""


def read_file(filename=''):
    """
    inside the function
    """
    with open(filename, encoding='utf-8') as f:
        line_list = f.readlines()
        for line in line_list:
            print(line.strip())
