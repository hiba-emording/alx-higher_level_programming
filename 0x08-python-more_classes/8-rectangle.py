#!/usr/bin/python3

"""
Define a class: Rectangle.
"""


class Rectangle:
    """
    A class defines a rectangle
    Attributes:
    number_of_instances (int): number of rectangle instances
    print_symbol: used for string representation
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle
        Args:
            width(int): the width
            height(int): the height
        """

        Rectangle.number_of_instances += 1
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the greatest area's rectangle

        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """returns string representation of rectangle"""
        if self.width == 0 or self.height == 0:
            return ''
        rect = ''
        print_symbol = str(self.print_symbol)

        for i in range(self.height):
            rect += print_symbol * self.width
            if i != self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """returns a string representation that can create a new rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """prints a message when rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
