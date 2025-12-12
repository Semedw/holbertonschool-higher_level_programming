#!/usr/bin/python3
"""
Inherits from
"""


def inherits_from(obj, a_class):
    """
    Inside the function
    """
    if isinstance(obj.__class__, a_class):
        subcls = obj.__class__
        if isinstance(subcls, a_class):
            return True
        return False
    return False
