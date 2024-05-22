#!/usr/bin/python3
"""Creates an Object from a “JSON file"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file

    Parameters:
    filename (str): The name of the file to convert to python object

    Returns:
    A python object
    """
    with open(filename, 'r') as file:
        data = json.load(file)

    return data


if __name__ == "__main__":
    filename = "out.json"
    load_from_json_file(filename)
