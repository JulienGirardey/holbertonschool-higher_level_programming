#!/usr/bin/python3
"""
square

this file contains the class Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this is a class Square with
    the size of square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[{}] {}/{}".format(Square.__name__, self.__size, self.__size)
