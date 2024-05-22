#!/usr/bin/python3

"""
class to define Student attributes
"""


class Student:
    """
    Student class

    to_json: creates a json-like dictionary

    Args:
        first_name: student's first name
        last_name: Student's last name
        age: Student's age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return vars(self)
