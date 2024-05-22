#!/usr/bin/python3
"""Adds all arguments to a Python list and then saves them to a file"""
import sys
from os.path import isfile

_save = __import__("5-save_to_json_file").save_to_json_file
_load = __import__("6-load_from_json_file").load_from_json_file


def main():
    """
    adds all arguments to a Python list and then saves them to a file

    Parameters:
    All command line arguements after the filename

    Return: None
    """
    if isfile('add_item.json'):
        obj_list = _load('add_item.json')
    else:
        obj_list = []

    for arg in sys.argv[1:]:
        obj_list.append(arg)

    _save(obj_list, 'add_item.json')


if __name__ == "__main__":
    main()
