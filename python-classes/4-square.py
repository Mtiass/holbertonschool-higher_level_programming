#!/usr/bin/python3
"""
This module defines Square as a class.
"""


class Square:
    """
    This is a class where a square is defined.

    Attributes:
        size: is a private instance attribute.
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        This is a public instance method to calculate the area of a square.
        """

        sqarea = self.__size ** 2
        return (sqarea)
