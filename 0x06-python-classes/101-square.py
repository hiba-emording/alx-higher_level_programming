#!/usr/bin/python3

"""Define a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a square instance.

        Args:
            size (int): The size of the square's side length.
            position (tuple): The position of the square.
        """
        self._size = size
        self._position = position

    @property
    def size(self):
        """Get or set the size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        elif value < 0:
            raise ValueError("Size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Get or set the position of the square."""
        return self._position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("Position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Return the area of the square."""
        return self._size ** 2

    def my_print(self):
        """Print the square using '#' character."""
        if self._size == 0:
            print("")
            return

        for i in range(self._position[1]):
            print("")

        for i in range(self._size):
            print(" " * self._position[0], end="")
            print("#" * self._size)

    def __str__(self):
        """Return the string representation of the square."""
        result = ""
        if self._size != 0:
            for i in range(self._position[1]):
                result += "\n"

            for i in range(self._size):
                result += " " * self._position[0]
                result += "#" * self._size
                if i != self._size - 1:
                    result += "\n"
        return result
