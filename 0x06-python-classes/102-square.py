#!/usr/bin/python3

"""Define a Square class for square representation and comparison."""


class Square:
    """Represents a square and defines comparisons."""

    def __init__(self, side_length=0):
        """
        Initialize a square instance.

        Args:
            side_length (int): The length of each side of the square.
        """
        self.side_length = side_length

    @property
    def side_length(self):
        """Get or set the side length of the square."""
        return self._side_length

    @side_length.setter
    def side_length(self, value):
        """Set the side length of the square."""
        if not isinstance(value, int):
            raise TypeError("Side length must be an integer")
        elif value < 0:
            raise ValueError("Side length must be >= 0")
        self._side_length = value

    def area(self):
        """Calculate and return the area of the square."""
        return self._side_length * self._side_length

    def __eq__(self, other):
        """Check if two squares have equal areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares have unequal areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if one square has a smaller area than the other."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square has a smaller or equal area than the other."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if one square has a greater area than the other."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square has a greater or equal area than the other."""
        return self.area() >= other.area()
