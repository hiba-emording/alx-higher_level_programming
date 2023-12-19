#!/usr/bin/python3

"""
Define a class: Square
"""


class Square:
    """
    A class to represent a square
    Attributes:
        __size (int): The size of each side of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
        - size (int): The size of each side of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
        - int: The size of each side of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
        - value (int): The size of each side of the square.
        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square (size * size).
        """
        return self.__size * self.__size
