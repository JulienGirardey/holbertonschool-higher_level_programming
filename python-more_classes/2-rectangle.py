#!/usr/bin/python3
"""
2-rectangle

That create a class that defines a rectangle
"""


class Rectangle:
    """
    class rectangle to defines a rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        That return the attribut
        """
        return self.__width

    @property
    def height(self):
        """
        That return the attribut
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        assigne new value at attribut
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """
        assigne new value at attribut
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        that display the area of rectangle
        """
        return (self.height * self.width)

    def perimeter(self):
        """
        that display the perimeter of rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2
