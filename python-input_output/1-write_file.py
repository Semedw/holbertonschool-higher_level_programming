#!/usr/bin/python3
"""
write a file
"""


def write_file(filename='', text=''):
    """
    inside the function
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        written_text = f.write(text)
