#!/usr/bin/python3
"""
Module Rectangle:
    Defines a class Rectangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle utilizing the functionalities of BaseGeometry.

    Attributes:
        __width (int): The width of the Rectangle.
        __height (int): The height of the Rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new Rectangle with specified width and height.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        returns area of Rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Returns:
        [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
