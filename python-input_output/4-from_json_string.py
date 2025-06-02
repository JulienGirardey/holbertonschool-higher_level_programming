#!/usr/bin/python3
"""
from_json_string

this module contains the
from_json_string function
"""
import json


def from_json_string(my_str):
    """
    this function return an object
    represented by a JSON string
    """
    return json.loads(my_str)
