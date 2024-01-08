#!/usr/bin/python3
"""
Module: lookup
This module provides a function to retrieve the attributes
     and methods of an object.
Functions:
- lookup(obj): Returns a list of attributes and methods of the given object.
"""


def lookup(obj):
    """
    A function that returns a list of attributes and
      methods of the given object.

    Args:
    - obj: Object to be listed.

    Returns:
    - A list containing the names of attributes and methods of the object.
    """
    return dir(obj)
