#!/usr/bin/python3
"""
rectangle file
"""


class BaseGeometry:
    """
    inside the base geometry class
    """

    def __init__(self, width, height):
        """
        init function
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
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """
    inheriting from basegeometry class
    """

    def __init__(self, width, height):
        """
        inside the init method
        """
        self.integer_validator("width", width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height
