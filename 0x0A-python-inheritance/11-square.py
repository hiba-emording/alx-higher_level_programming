#!/usr/bin/python3
"""
Module Square:
    Defines a class Square that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square utilizing the functionalities of Rectangle.

    Attributes:
        __size (int): The size of square.
    """

    def __init__(self, size):
        """
        Initializes a new Square with specified size.

        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns:
        area of square
        """
        return (self.__size ** 2)

    def __str__(self):
        """
        Returns:
        [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
