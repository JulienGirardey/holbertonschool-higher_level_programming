#!/usr/bin/python3
"""
read_file

this module contains...
"""


def read_file(filename=""):
    """
    this function open file and print
    it content
    """
    with open(filename, "r") as file:
        content = file.read()
        print(content, end="")
