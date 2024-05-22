#!/usr/bin/python3
"""Converts a Python object to a JSON string"""

import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON string

    Parameters:
    my_obj: The Python object to convert to JSON

    Returns:
    The JSON: representation of the object
    """
    return json.dumps(my_obj)


if __name__ == "__main__":
    to_json_string()
