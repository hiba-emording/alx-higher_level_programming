#!/usr/bin/python3
"""
Student to JSON
Defines a class: Student
"""


class Student:
    """A class that represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        A function to Retrieve a dictionary representation of a Student

        Args:
        - attrs (list): A list of strings representing attribute names.
                        If None, all attributes will be retrieved.

        Returns:
        A dictionary containing the specified attributes of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
