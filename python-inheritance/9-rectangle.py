#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a rectangle """

    def __init__(self, width, height):
        """creaty a new rectangle"""
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("width", width)
        self.__width = width

    def area(self):
        """Return the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Return the print() and str() of a rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__height) + "/" + str(self.__width)
        return string
