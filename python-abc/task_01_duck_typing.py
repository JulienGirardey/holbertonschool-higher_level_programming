#!/usr/bin/python3
"""
task_01_duck_typing

this file contains 3 class:
Shape, Circle, Rectangle
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    this class contains 2 abstractmethod:
    area and perimeter
    """
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    this class contains 2 abstractmethod:
    area, returning the area of the circle and
    perimeter, returning the perimeter of the circle
    """
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    this class contains 2 abstractmethod:
    area, returning the area of the rectangle and
    perimeter, returning the perimeter of the rectangle.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(obj):
    """
    this function print the result of
    area and perimeter method
    """
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
