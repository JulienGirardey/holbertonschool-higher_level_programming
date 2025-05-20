#!/usr/bin/python3
"""
6-square

That create class square to handle object
"""


class Square:
    """
    Class Square create square object
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        create an instance of object with these parameter
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Return private attribut to access it indirectly
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Change the value of private attribut indirectly
        """
        if (not isinstance(value, tuple) or
            len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        That returns the current square area
        """
        return self.size ** 2

    def my_print(self):
        """
        That print square with '#' symbol and add space to position
        """
        if self.size == 0:
            print()
            return
        for col in range(self.position[1]):
            print("")
        for i in range(self.size):
            for row in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
