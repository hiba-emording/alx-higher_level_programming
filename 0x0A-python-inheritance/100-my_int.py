#!/usr/bin/python3
"""
Module My Integer:
Defines a rebel integer class MyInt with inverted
equality and inequality operators.
"""


class MyInt(int):
    """
    Represents a rebel integer class with inverted equality and inequality.

    Inherits from int and overrides the == and != operators.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator ==.

        Args:
            other (Any): The value to compare with.

        Returns:
            True if the values are not equal,
            False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator !=.

        Args:
            other (Any): The value to compare with.

        Returns:
            True if the values are equal,
            False otherwise.
        """
        return super().__eq__(other)
