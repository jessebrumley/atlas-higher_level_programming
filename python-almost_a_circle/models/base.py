#!/usr/bin/python3

"""Defines a base class """
import json


class Base:
    """
    This represents a base template for all classes in this project.

    Private Class Attributes:
        __nb_object (int): Number of Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of a string to a file."""

        if list_objs is None or list_objs == []:
            with open(f'{cls.__name__}.json', 'w') as f:
                pass
        else:
            with open(f'{cls.__name__}.json', 'w') as f:
                f.write(Base.to_json_string(list_objs))
