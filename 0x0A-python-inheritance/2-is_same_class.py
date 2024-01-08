#!/usr/bin/python3
"""
Module: Exact Same Object
This module contains a function to check if
an object is an instance of a specified class.

Functions:
    is_same_class(obj, a_class)
        Check if the object is an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is an instance of the specified class.

    Args:
    - obj: The object.
    - a_class: The class.

    Returns:
    - True if obj is an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False
