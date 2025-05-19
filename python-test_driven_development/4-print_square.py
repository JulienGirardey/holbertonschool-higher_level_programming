#!/usr/bin/python3
"""
print_square

That prints a square with the character # when lenght is the size of the square
"""


def print_square(size):
    """
    This function handle some exeption
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    col = 0
    while col < size:
        row = 0
        while row < size:
            print("#", end="")
            row += 1
        print()
        col += 1
