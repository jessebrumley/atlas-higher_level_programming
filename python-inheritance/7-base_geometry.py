#!/usr/bin/python3
"""Defines a base geometry class """


class BaseGeometry:
    """Defines a base geometry class"""

    def __init__(self, lst=None):
        if lst is None:
            self.lst = []
        else:
            self.lst = lst[:]

    def append(self, item):
        self.lst.append(item)

    def print_sorted(self):
        print(sorted(self.lst))

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))