#!/usr/bin/python3

def print_list_integer(my_list=[]):
    number = len(my_list)
    for i in range(number):
        print("{:d}".format(my_list[i]))
