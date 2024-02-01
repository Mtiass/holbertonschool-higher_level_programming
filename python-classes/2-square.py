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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
