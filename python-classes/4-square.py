#!/usr/bin/python3
"""
4-square

That create class square to handle object
"""


class Square:
    """
    Class Square create square object
    """
    def __init__(self, size=0):
        """
        create an instance of object with these parameter
        """
        self.__size = size

    @property
    def size(self):
        """
        Return private attribut to access it indirectly
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Change the value of private attribut indirectly
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        That returns the current square area
        """
        return self.__size ** 2
