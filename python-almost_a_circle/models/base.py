#!/usr/bin/python3

"""The “base” of all other classes in this project"""

Class Base:
    """
    Base Class model used as template for all other classes in this project
    
    Class Attributes:
        __nb_object (int): Number of Bases.
    """
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        if id is not None:
            self.id=id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
