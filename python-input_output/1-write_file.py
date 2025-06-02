#!/usr/bin/python3
"""
write_file

this module contains function
write_file to write text in to file
and return the number of arguments written
"""


def write_file(filename="", text="", endcoding="utf-8"):
    """
    this function return the numbers of arguments
    written in the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
    return len(text)
