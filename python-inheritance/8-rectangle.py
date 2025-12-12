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
        initializing class
        """
        self.__width = width
        self.__height = height

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
            raise TypeError('<name> must be an integer')
        if value <= 0:
            raise ValueError('<name> must be greater than 0')

