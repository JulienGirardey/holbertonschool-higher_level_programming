#!/usr/bin/python3
"""
to_json_string

this module contains the to_json_string
function
"""
import json


def to_json_string(my_obj):
    """
    this function returns the JSON
    representation of an object(string)
    """
    return json.dumps(my_obj)
