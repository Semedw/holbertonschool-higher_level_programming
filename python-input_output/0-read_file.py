#!/usr/bin/python3
"""
reading a text file
"""


def read_file(filename=''):
    """
    inside the function
    """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line.strip())
