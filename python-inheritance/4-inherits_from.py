#!/usr/bin/python3
"""
Inherits from
"""


def inherits_from(obj, a_class):
    """
    Inside the function
    """
<<<<<<< HEAD
    if type(obj) == 
=======
    if obj.__class__ == a_class:
        return False
    return issubclass(obj.__class__, a_class)
>>>>>>> d34d77a4bed289a4fe01e055525cc4dc4483cf2f
