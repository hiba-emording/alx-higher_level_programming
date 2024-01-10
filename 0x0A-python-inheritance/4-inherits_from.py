#!/usr/bin/python3
"""
Module: Only Subclass
This module contains a function to check if an object is
an inherited instance of a specified class.

Functions:
    inherits_from(obj, a_class)
        Check if the object is inherited instance of the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an inherited instance of a specified class.

    Args:
    - obj: The object.
    - a_class: The class.

    Returns:
    - True if obj is an inherited instance of a_class.
    - False otherwise.
    """
    if isinstance(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
