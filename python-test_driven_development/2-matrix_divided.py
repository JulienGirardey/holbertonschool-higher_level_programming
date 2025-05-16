#!/usr/bin/python3
"""
matrix_divided.py
This module provides a function to divide
all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by
    a given number, rounded to 2 decimal places.
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row_check in matrix:
        if not isinstance(row_check, list):
            raise TypeError("matrix must be a matrix"
                            "(list of lists) of integers/floats")
        for elem_check in row_check:
            if not isinstance(elem_check, (int, float)):
                raise TypeError("matrix must be a matrix"
                                "(list of lists) of integers/floats")
        if not len(row_check) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(num / div, 2) for num in row] for row in matrix]
