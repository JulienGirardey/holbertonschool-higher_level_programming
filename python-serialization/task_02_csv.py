#!/usr/bin/python3
"""
this module contains 1 function
convert_csv_to_json and import 2 modules
csv and json
"""
import csv
import json


def convert_csv_to_json(filename):
    """
    this function convert csv file in to
    json file using csv and json module
    """
    try:
        with open(filename, "r") as file:
            csv_reader = csv.DictReader(file)
            data = []
            for row in csv_reader:
                data.append(dict(row))
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        return True
    except FileNotFoundError:
        return False
