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
        Returns a list of JSON strings
        """
        if list_dictionaries is None:
            return []
        return [json.dumps(d) for d in list_dictionaries]

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)
        objects = []
        if list_objs is not None:
            for obj in list_objs:
                objects.append(obj.to_dictionary())
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(objects))