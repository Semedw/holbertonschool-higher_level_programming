#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """
    Inside the rectangle class
    """
    
    def __init__(self, width, height):
        """
        Initialize when object is created
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Property of width
        """
        self.__width = width

    @property
    def height(self):
        """
        Property of height
        """
        self.__height = height
    
    @width.setter
    def width(self, value):
        """
        Width setter
        """
        if not isinstance(value, int):
            raise TypeError('width must be integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self__height = value
