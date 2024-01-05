#!/usr/bin/python3
"""
Defines a class: LockedClass
"""


class LockedClass:
    """represents a locked class - only first_name attribute is allowed"""
    __slots__ = ["first_name"]
