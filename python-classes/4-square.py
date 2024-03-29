#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Class representing a square"""

    def __init__(self, size=0):
        """Initializing a square

        Args: size(int): The size of the new square. Must be an integer.
        """
        self.size = size

    @property
    def size(self):
        """Gets and sets the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)
