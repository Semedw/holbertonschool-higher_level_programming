#!/usr/bin/python3
"""
is same class
"""


def is_same_class(obj, a_class):
    """
    check if the object is instance of the given class
    """
    if obj.__class__ == a_class:
        return True
    return False
