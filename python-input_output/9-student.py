#!/usr/bin/python3
"""
This module defines Student as a class.
"""


class Student:
    """
    This is a class defines a student as Student.

    Attributes:
        first_name: is a public instance attribute.
        last_name: is a public instance attribute.
        age: is a public instance attribute.
    """

    def __init__(self, first_name, last_name, age):
        """
        This is a special method that is automatically called when an
        object of a class is instantiated.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This is a public method that retrieves a dictionary
        representation of a Student instance.
        """
        return (self.__dict__)
