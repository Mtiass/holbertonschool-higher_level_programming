#!/usr/bin/python3
"""
This module defines Square as a class inherited from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is a class where Square is defined.
    """

    def __init__(self, size):
        """
        This initializes a new instance of Square.

        Arguments:
            size: is a private instance attribute which defines the
            square's size.
        """

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        This is a public instance method that returns a square's area.
        """

        return (self.__size * self.__size)

    def __str__(self):
        """
        This is a method that returns a human-readable string,
        that is a representation of the object.
        """

        desc = "[Rectangle] "
        desc += str(self.__size) + "/" + str(self.__size)
        return (desc)
