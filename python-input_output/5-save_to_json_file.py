#!/usr/bin/python3
"""
save_to_json_file

this module contains the
save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    this function write an object
    to a text file using JSON representation
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
