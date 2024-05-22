#!/usr/bin/python3

"""
Defines class of students
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

    def to_json(self, attrs=None):
        student_dict = vars(self)
        if attrs is not None:
            new_dict = {}
            for key in attrs:
                if key in student_dict:
                    new_dict[key] = student_dict[key]
            return new_dict
        return student_dict
