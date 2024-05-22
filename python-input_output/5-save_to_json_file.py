#!/usr/bin/python3
"""Writes an Object to a text file, using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation

    Parameters:
    my_obj: The Python object to convert to JSON & write to file
    filename (str): The name of the file to write to or create

    Returns:
    None
    """

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))


if __name__ == "__main__":
    my_obj = {"key": "value"}
    filename = "output.json"
    save_to_json_file()
