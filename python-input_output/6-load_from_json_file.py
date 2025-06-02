#!/usr/bin/python3
"""
load_from_json_file

this module contains
load_from_json_file function
"""
import json


def load_from_json_file(filename):
	"""
	this function return an object
	from a JSON file
	"""
	with open(filename, "r") as file:
		return json.load(file)
