#!/usr/bin/python3
"""
This module defines Rectangle as a class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This defines Rectangle as a class.

    Attributes:
        width: This is a private instance attribute that defines the
        Rectangle's width.

        height: is a private instance attribute which defines the
        Rectangle's height.
    """

    def __init__(self, width, height):
        """
        This function initializes a Rectangle instance, having width and
        height as parameters.
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
