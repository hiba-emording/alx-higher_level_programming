#!/usr/bin/python3
"""
Print Name Module

This module provides functionality to print a given name.

Functions:
    say_my_name(first_name, last_name=""):
        Prints the full name using the provided first and last names.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name using the provided first and last names.

    Args:
    - first_name (str): The first name.
    - last_name (str): The last name. Defaults to empty string.

    Raises:
    - TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
