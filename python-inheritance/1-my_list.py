#!/usr/bin/python3
"""Defines an inherited list"""


class MyList(list):
    """Defines a list"""

    def print_sorted(self):
        """Prints a list in ascending order"""
        print(sorted(self))
