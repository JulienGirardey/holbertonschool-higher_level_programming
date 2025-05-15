#!/usr/bin/python3
"""
matrix_divided.py

this module divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, (list)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    result = []
    for row in matrix:
        new_row = []
        if not len(row) == len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(elem / div, 2))
        result.append(new_row)
    return result
