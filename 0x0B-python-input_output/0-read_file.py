#!/usr/bin/python3
"""
File Reader Module
contains a function that reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
