#!/usr/bin/python3
"""
Write to file  Module
contains a function that writes a string to a text file (UTF8) and
returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8)
    Args:
        filename (str)
        text (str)
    Return:
        Number of chars wrritten.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
