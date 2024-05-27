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

    def update(self, *args, **kwargs):
        """
        Updates Square and assigns an argument to each attribute
        """
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        return a dictionary of the calling instance's attributes
        """
        id = self.id
        size = self.width
        x = self.x
        y = self.y
        return {'id': id, 'size': size, 'x': x, 'y': y}
