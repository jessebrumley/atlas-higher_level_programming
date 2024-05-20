#!/usr/bin/python3
"""Defines a base geometry class """


class BaseGeometry:
    """Defines a base geometry class"""

    def area(self):
        """defines area of BaseGeometry class """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a value as an integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
