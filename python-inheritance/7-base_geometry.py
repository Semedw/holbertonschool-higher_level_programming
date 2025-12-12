#!/usr/bin/python3
"""
empty class
"""


class BaseGeometry:
    """
    inside the base geometry class
    """
    
    def __init__(self, width, height):
        """
        inside the init method
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        raises an exeption
        """
        return self.__width * self.__height

    def integer_validator(self, name, value):
        """
        inside the function
        """
        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
