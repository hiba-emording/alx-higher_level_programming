#!/usr/bin/python3
"""
Class to JSON
Defines a Python function for converting a class instance to a
JSON-compatible dictionary.
"""


def class_to_json(obj):
    """
    A function that Returns the dictionary representation
    of a simple data structure.

    Args:
        obj: The object to be represented.

    Returns:
        A dictionary containing the attributes and values of the input object.
    """
    return obj.__dict__
