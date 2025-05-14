#!/usr/bin/python3

def add_integer(a, b=98):
    """
    that adds 2 integer, transform float in to integer and handle wrong type
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    result = a + b
    return result
