#!/usr/bin/python3
"""
read_file

this module contains...
"""


def read_file(filename="", endcoding="utf-8"):
    """
    this function open file and print
    it content
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
