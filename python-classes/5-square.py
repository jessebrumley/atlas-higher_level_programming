#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Class representing a square"""

    def __init__(self, size=0):
        """Initializing a square

        Args:
            size(int): The size of the new square. Must be an integer.
            position (int, int): The position of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square to stdout using #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
