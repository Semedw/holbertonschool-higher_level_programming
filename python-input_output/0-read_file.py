#!/usr/bin/python3
"""
reading a text file
"""


def read_file(filename=''):
    """
    inside the function
    """
    with open(filename, encoding='utf-8') as f:
        read_text = f.read()
        print(read_text.strip())
