#!/usr/bin/python3
"""
Add items to a list and save to JSON file Module
"""
import sys
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


def load_from_json_file(filename):
    """
    Creates/Loads an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        The object loaded from the JSON file.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


my_list = load_from_json_file('add_item.json') or []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, 'add_item.json')
