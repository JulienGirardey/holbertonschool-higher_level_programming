#!/usr/bin/python3
"""
inherits_from

this file contains inherits_from() method
"""


def inherits_from(obj, a_class):
    """
    return true if obj have not the same type as a_class
    """
    return type(obj) is not a_class
