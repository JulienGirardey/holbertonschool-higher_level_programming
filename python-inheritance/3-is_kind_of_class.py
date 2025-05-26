#!/usr/bin/python3
"""
is_kind_of_class

that return True if the object is an instance of,
or id the object is an instance of a class that
inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    return true or False if obj isinstance  of a_class
    """
    return isinstance(obj, a_class)
