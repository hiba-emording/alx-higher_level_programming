#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    keys_del = []

    for key, val in a_dictionary.items():
        if val == value:
            keys_del.append(key)

    for key in keys_del:
        del a_dictionary[key]

    return a_dictionary
