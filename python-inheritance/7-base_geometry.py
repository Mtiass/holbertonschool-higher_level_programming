#!/usr/bin/python3
"""
This module defines BaseGeometry as a class.
"""


class BaseGeometry:
    """
    This is a class.
    """

    def area(self):
        """
        This is a public instance method.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This is a public instance method that validates value.
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
