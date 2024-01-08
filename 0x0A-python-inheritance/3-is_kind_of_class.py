#!/usr/bin/python3
"""
Module: Is kind of class
This module contains a function to check if an object is an instance
or inherited instance of a specified class.

Functions:
    is_kind_of_class(obj, a_class)
        Check if the object is an instance or
        inherited instance of the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance or
    inherited instance of a specified class.

    Args:
    - obj: The object.
    - a_class: The class.

    Returns:
    - True if obj is an instance of a_class, or
      Inherited instance of a class.
    - False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
