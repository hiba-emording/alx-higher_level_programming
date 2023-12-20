#!/usr/bin/python3

"""Define a MagicClass that matches a provided bytecode by Holberton."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance.

        Args:
            radius (float or int): The radius of the circle in the MagicClass.
        """
        self._MagicClass__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculate and return the area of the circle in the MagicClass."""
        return (self._MagicClass__radius ** 2 * math.pi)

    def circumference(self):
        """
        Calculate and return the circumference of the circle in the MagicClass.
        """
        return (2 * math.pi * self._MagicClass__radius)
