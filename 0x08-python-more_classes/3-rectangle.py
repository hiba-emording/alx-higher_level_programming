#!/usr/bin/python3

"""
Define a class: Rectangle.
"""


class Rectangle:
    """A class defines a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle
        Args:
            width(int): the width
            height(int): the height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Set the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """returns string representation of rectangle"""
        if self.width == 0 or self.height == 0:
            return ''
        rect = ''
        for i in range(self.height):
            rect += '#' * self.width + '\n'
        return rect
