#!/usr/bin/python3
"""
write_file

this module contains function
write_file to write text in to file
and return the number of arguments written
"""


def write_file(filename="", text=""):
    """
    this function return the numbers of arguments
    written in the file
    """
    with open(filename, "w") as file:
        file.write(text)
    return len(text)
