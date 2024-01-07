#!/usr/bin/python3
"""
Addition Function Module

This module provides functionality for adding two numbers.

Functions:
    add_integer(a, b=98):
        Adds two integers or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    a (int or float): First number.
    b (int or float, optional): Second number, default'98'.

    Returns:
    The addition of a and b: (int).

    Raises:
    TypeError: If 'a' or 'b' is not an int or float.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
