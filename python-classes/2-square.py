#!/usr/bin/python3
class Square:
    """Class representing a square"""
    def __init__(self, size=0):
        """Initializing a square

        Args: size(int): The size of the new square. Must be an integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
