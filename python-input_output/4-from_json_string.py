#!/usr/bin/python3
"""Converts a JSON string to a Python Data Structure Object"""

import json


def from_json_string(my_str):
    """
    Converts a JSON string to a Python Data Structure Object

    Parameters:
    my_str The JSON string to convert to Python Object

    Returns:
    The python object
    """

    return json.loads(my_str)


if __name__ == "__main__":
    from_json_string()
