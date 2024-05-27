#!/usr/bin/python3

"""The “base” of all other classes in this project"""


class Base:
    """
    Base Class model used as template for all other classes in this project

    Class Attributes:
        __nb_objects (int): Number of Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns a list of JSONified dictionaries
        """
        empty_list = "[]"
        if list_dictionaries is None:
            return empty_list
        return json.dumps(list_dictionaries)
