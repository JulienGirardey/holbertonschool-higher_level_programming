#!/usr/bin/python3
"""
basic_serialization

this module contains 2 functions
to serialize and deserialize
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    this function serialize and save
    data to the specified file
    """
    with open(filename, "w") as file:
        json.dump(data, file)
    pass


def load_and_deserialize(filename):
    """
    this function load and deserialize
    data from the specified file
    """
    with open(filename, "r") as file:
        return json.load(file)
    pass
