#!/usr/bin/python3
"""
Print Square Function Module

This module provides functionality for printing a square of a given size by #.

Functions:
    print_square(size):
        Prints a square with the character '#'.
"""


def print_square(size):
    """
    Prints a square of a given size with the character '#'.

    Args:
    - size (int): The size length of the square.

    Raises:
    - TypeError: If size is not an int.
    - ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end='') for j in range(size)]
        print('')
