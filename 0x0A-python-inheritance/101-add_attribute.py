#!/usr/bin/python3
"""
Module: Can I
Defines a function add_attribute
    adds a new attribute to an object if possible.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if possible; raises TypeError otherwise.

    Args:
        obj (object): The object to add the attribute to.
        attr (str): The attribute name.
        value (Any): The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
