#!/usr/bin/python3
"""Function that divides all elements of a matrix by a given number.
Validates the structure of the matrix and the type of each element.
Ensures all rows are of equal size and that the divisor is a number.
Raises TypeError or ZeroDivisionError with precise messages when needed.
Returns a new matrix with each result rounded to 2 decimal places."""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix by a given number.
Validates the structure of the matrix and the type of each element.
Ensures all rows are of equal size and that the divisor is a number.
Raises TypeError or ZeroDivisionError with precise messages when needed.
Returns a new matrix with each result rounded to 2 decimal places."""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row_check in matrix:
        if not isinstance(row_check, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for elem_check in row_check:
            if not isinstance(elem_check, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not len(row_check) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    result = []
    for row in matrix:
        new_row = []
        for elem in row:
            new_row.append(round(elem / div, 2))
        result.append(new_row)
    return result
