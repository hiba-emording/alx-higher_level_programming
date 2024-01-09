#!/usr/bin/python3
"""
Append to file  Module
contains a function that appends a string at the end of a text file (UTF8) and
returns the number of characters appended.
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file (UTF8)
    Args:
        filename (str)
        text (str)
    Return:
        Number of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
