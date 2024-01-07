#!/usr/bin/python3
"""
Text Indentation Module

This module provides functionality to print text with two newlines
    after certain punctuation marks ('.', '?', ':').

Functions:
    text_indentation(text):
        Prints the given text with 2 newlines after specific punctuation marks.
"""


def text_indentation(text):
    """
    Prints the provided text with 2 newlines after ('.', '?', ':') characters.

    Args:
    - text (str): The input.

    Raises:
    - TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    chars = ['.', '?', ':']
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1
    while c < len(text):
        print(text[c], end='')
        if text[c] == "\n" or text[c] in chars:
            if text[c] in chars:
                print('\n\n', end='')
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
