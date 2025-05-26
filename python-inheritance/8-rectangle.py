#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
rectangle

this file contains class Rectangle that
inherits form BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    this is a class Rectangle contains
    width and height of the rectangle
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
