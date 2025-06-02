#!/usr/bin/python3
"""
student

this module contains
Student class
"""


class Student:
    """
    this class contains 2 methods:
    init to create an instance of this class,
    to_json to return a dictionary representation
    of a student instance
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
