#!/usr/bin/python3
"""
sqaure that was inherited from rectangle
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    inside the square
    """
    
    def __init__(self, size):
        """
        inside the init method
        """
        self.integer_validator("size", size)

        self.__size = size
