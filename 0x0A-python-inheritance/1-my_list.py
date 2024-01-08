#!/usr/bin/python3
"""
MODULE: MY LIST
This module contains the MyList class, a subclass of list,
with a method to print a sorted list.
"""


class MyList(list):
    """
    Class: list
    Subclass: MyList
     - Contains a public instance method to
       print a list sorted in ascending order.
    """
    def __init__(self):
        """ A function for object initialization"""
        super().__init__()

    def print_sorted(self):
        """ A function to sort the list and print it"""
        sorted_list = sorted(self)
        print(sorted_list)
