#!/usr/bin/python3
"""
To JSON string Module
"""
import json


def to_json_string(my_obj):
    """
    Converts the given object to its JSON representation.

    Args:
        my_obj: the object to convert

    Return:
        (str): The json repr of obj.
    """
    return json.dumps(my_obj)
