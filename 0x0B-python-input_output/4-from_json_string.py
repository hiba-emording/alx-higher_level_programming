#!/usr/bin/python3
"""
To JSON object Module
"""
import json


def from_json_string(my_str):
    """
    Converts the given JSON string to its Obj.

    Args:
        my_str: the json string to convert

    Return:
        The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
