#!/usr/bin/python3
"""
Save Obj to Json file Module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object using JSON repr to a text file.

    Args:
    - my_obj: The object to be written to the file.
    - filename (str): The name of the file.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
