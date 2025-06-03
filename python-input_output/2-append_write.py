#!/usr/bin/python3
"""
append_write

this module contains the
append_write function
"""


def append_write(filename="", text=""):
    """
    this function append a text
    at file and return the length
    of the text append
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
    return len(text)
