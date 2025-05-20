#!/usr/bin/python3
"""
5-square

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

    def my_print(self):
        """
        That print square with '#' symbol
        """
        i = 0
        if self.size == 0:
            print()
        for i in range(self.size):
            j = 0
            for j in range(self.size):
                print("#", end="")
            print("")
