#!/usr/bin/python3
"""
rectangle file
"""


class Rectangle(BaseGeometry):
    """
    inheriting from basegeometry class
    """

    def __init__(self, width, height):
        """
        inside the init method
        """
        self.__width = width
        self.__height = height
