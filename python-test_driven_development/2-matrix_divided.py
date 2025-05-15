#!/usr/bin/python3
"""Function that divides all elements of a matrix by a given number.
Validates the structure of the matrix and the type of each element.
Ensures all rows are of equal size and that the divisor is a number.
Raises TypeError or ZeroDivisionError with precise messages when needed.
Returns a new matrix with each result rounded to 2 decimal places."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.
Ensures proper types and structure, and rounds results to 2 decimals.
Raises TypeError or ZeroDivisionError on invalid input."""

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
