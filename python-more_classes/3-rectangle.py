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

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__height = height
        self.__width = width

    def __str__(self):

        if self.__width == 0 or self.__height == 0:
            return ("")

        string = ""
        for row in range(self.__height):
            for column in range(self.__width):
                string += "#"
            if row < self.__height - 1:
                string += '\n'
        return (string)

    def __repr__(self):

        if self.__width == 0 or self.__height == 0:
            return ("")

        mod = self.__module__
        clname = self.__class__.__name__
        return ("<{}.{} obect at {}>".format(mod, clname, hex(id(self))))

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

    def area(self):
        """
        This is a public method that returns the rectangle's area.
        """

        area = self.__height * self.__width
        return (area)

    def perimeter(self):
        """
        This is a public method that returns the rectangle's perimeter.
        """

        if self.__height == 0 or self.__width == 0:
            perimeter = 0
            return (perimeter)

        perimeter = 2 * (self.__height + self.__width)
        return (perimeter)
