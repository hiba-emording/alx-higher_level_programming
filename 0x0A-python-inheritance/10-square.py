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
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
