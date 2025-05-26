#!/usr/bin/python3
"""
is_same_class.py

that return True if the object is
exactly an instance of the specified calss
"""


def is_same_class(obj, a_class):
    """
    return True if the object is exactly
    an instance of the specified class
    """
    return type(obj) is a_class
