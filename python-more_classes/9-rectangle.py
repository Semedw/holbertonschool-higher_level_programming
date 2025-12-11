#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """
    Inside the rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize when object is created
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Property of width
        """
        return self.__width

    @property
    def height(self):
        """
        Property of height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Width setter
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Height setter
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """
        This method calculates area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        This method returns the perimeter of rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """
        Printing rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return ''
        s = ''
        for i in range(self.__height):
            s += str(self.print_symbol) * self.__width + '\n'

        return s.strip()

    def __repr__(self):
        """
        Representation of rectangle
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Executed when the object is deleted
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        height = size ** (1/2)
        width = size ** (1/2)
        return cls(height, width)
