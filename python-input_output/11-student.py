#!/usr/bin/python3

"""
Module containing Student class
"""

class Student:
    """
    Student class with to_json and reload_from_json methods

    Attributes:
        first_name (str): Student's first name
        last_name (str): Student's last name
        age (int): Student's age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student object with given attributes.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts the Student object to a JSON-like dictionary.

        Args:
            attrs (list[str], optional): List of attribute names to include in the output dictionary. Defaults to None, meaning all attributes will be included.

        Returns:
            dict: A dictionary representation of the Student object, optionally filtered by the provided attribute names.
        """
        if attrs is None:
            return {k: v for k, v in vars(self).items() if not k.startswith('_')}
        else:
            return {attr: getattr(self, attr) for attr in attrs}

    def reload_from_json(self, json):
        """
        Reloads the Student object from a JSON-like dictionary.

        Args:
            json (dict): A dictionary representing the state of the Student object.
        """
        for key, value in json.items():
            setattr(self, key, value)
