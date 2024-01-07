#!/usr/bin/python3
"""
Unittests for max_integer([..]).

This module contains unittests for the max_integer function.
It checks different cases to verify the correctness of max_integer function.
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Define unittests for max_integer([..]).

    This class contains various test cases to validate
        the behavior of the max_integer function.
    """

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered), 5)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 4, 5, 3, 2]
        self.assertEqual(max_integer(unordered), 5)

    def test_max_at_beginning(self):
        """Test a list with the maximum value at the beginning."""
        max_at_beginning = [9, 3, 6, 4, 2]
        self.assertEqual(max_integer(max_at_beginning), 9)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.22, 6.77, -20.123, 18.9, 6.0]
        self.assertEqual(max_integer(floats), 18.9)

    def test_ints_and_floats(self):
        """Test a list of mixed ints and floats."""
        ints_and_floats = [1.22, 18.9, -9, 18, 7, 16]
        self.assertEqual(max_integer(ints_and_floats), 18.9)

    def test_string(self):
        """Test a string with characters."""
        string = "Willy"
        self.assertEqual(max_integer(string), 'y')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["My", "name", "is", "ALEXANDER", "HAMILTON"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_negative_values(self):
        """Test a list with negative values."""
        negative_values = [-5, -10, -20, -30, -1]
        self.assertEqual(max_integer(negative_values), -1)

    def test_duplicate_values(self):
        """Test a list with duplicate values."""
        duplicate_values = [6, 9, 6, 6, 9, 9]
        self.assertEqual(max_integer(duplicate_values), 9)

    def test_large_values(self):
        """Test a list with large values."""
        large_values = [9999999999, 10000000000, 8888888888]
        self.assertEqual(max_integer(large_values), 10000000000)

    def test_negative_floats(self):
        """Test a list with negative floating-point numbers."""
        negative_floats = [-3.5, -7.8, -1.2, -9.0]
        self.assertEqual(max_integer(negative_floats), -1.2)


if __name__ == '__main__':
    unittest.main()
