#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dictionary = {'I': 1, 'V': 5, 'X': 10,
                        'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0

    for char in reversed(roman_string):
        curr = roman_dictionary[char]
        if curr >= prev:
            total = total + curr
        else:
            total = total - curr
        prev = curr

    return total
