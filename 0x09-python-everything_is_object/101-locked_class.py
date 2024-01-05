#!/usr/bin/python3
"""
Defines a class: LockedClass
"""


class LockedClass:
    """represents a locked class - only first_name attribute is allowed"""
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(
                    f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)
