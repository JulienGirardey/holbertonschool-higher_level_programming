#!/usr/bin/python3
"""
pickle

this module contains 1 class
and 3 methods
"""
import pickle


class CustomObject:
    """
    this class contains 3 methods,
    display, serialize and deserialize
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}\nAge: {}\nIs Student: {}".format
              (self.name, self.age, self.is_student))

    def serialize(self, filename):
        if not filename:
            return None
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        if not filename:
            return None
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
