#!/usr/bin/python3

"""
A subclass Square that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A subclass Square that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        id = self.id
        x = self.x
        y = self.y
        size = self.width
        return "[Square] ({0}) {1}/{2} - {3}".format(id, x, y, size)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
