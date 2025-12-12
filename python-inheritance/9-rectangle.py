#!/usr/bin/python3
"""
rectangle file
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def __str__(self):
        """
        inside the str method
        """
        return f'[Rectangle] {self.__width/self.__height}'
