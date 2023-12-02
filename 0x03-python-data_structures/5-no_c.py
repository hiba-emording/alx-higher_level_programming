#!/usr/bin/python3

def no_c(my_string):
    translation_table = {ord(char): None for char in 'cC'}
    new_string = my_string.translate(translation_table)
    return new_string
