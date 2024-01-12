#!/usr/bin/python3
"""
Module: geometry
Defines a class: BaseGeometry
"""


class BaseGeometry:
    """ represents a class: BaseGeometry """
    def area(self):
        """ Not implemented function that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A function to validate value

        Args:
        name (str)
        value (int)
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
