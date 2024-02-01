#!/usr/bin/python3
"""
This module defines Square as a class.
"""


class Square:
    """
    This is a class where a square is defined.

    Attributes:
        size: is a private instance attribute.
        position: is a private instance attribute as well.
    """

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        This is a public instance method to calculate the area of a square.
        """

        sqarea = self.__size * self.__size
        return (sqarea)

    def my_print(self):
        """
        This is a public instance method to print in stdout a square using #.
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i2 in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
