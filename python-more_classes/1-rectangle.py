#!/usr/bin/python3
"""
This module defines a class as Rectangle.
"""


class Rectangle:
    """
    This is an empty class that defines a rectangle.

    Attributes:
        width: is a private instance attribute that defines the
        Rectangle's width.
        height: is a private instance attribute which defines the
        Rectangle's height.
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @property
    def height(self):
        return (self.__height)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
