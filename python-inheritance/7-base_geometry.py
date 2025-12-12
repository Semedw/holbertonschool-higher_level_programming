#!/usr/bin/python3
"""
empty class
"""


class BaseGeometry:
    """
    inside the base geometry class
    """
    
    def area(self):
        """
        raises an exeption
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        inside the function
        """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
        if isinstance(value, bool):
            raise TypeError(f'{name} must be an integer')
