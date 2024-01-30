#!/usr/bin/python3

"""Defines a base class """

class Base:
    """
    Private Class Attributes:
        __nb_object (int): Number of Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = Base.__nb_objects