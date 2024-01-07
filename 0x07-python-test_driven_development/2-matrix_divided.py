#!/usr/bin/python3
"""
Matrix Division Module

This module provides functionality to perform division operation on matrices.

Functions:
    matrix_divided(matrix, div):
        Divides all elements in the matrix by a given divisor.
"""


def matrix_divided(matrix, div):
    """
    A function to divide all elements in matrix by a given divisor.
    Args:
    - matrix (list): A matrix (list of lists) containing integers or floats.
    - div (int/float): The divisor.
    Returns:
    - list: A new matrix with elements divided by the divisor,
            rounded to 2 decimal places.
    Raises:
    - TypeError: If the matrix is not a list of lists containing integers
                    or floats, or if the divisor is not a number.
    - ZeroDivisionError: If the divisor is zero.
    """
    if (
        not isinstance(matrix, list) or
        matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all(
            isinstance(x, int) or isinstance(x, float)
            for x in [i for row in matrix for i in row]
            )
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in row] for row in matrix]
