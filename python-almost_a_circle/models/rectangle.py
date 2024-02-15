#!/usr/bin/python3
"""
This module defines the class Rectangle that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a class that inherits from Base.

    Attributes:
        width: is a private instance attribute,
        represents the rectangle's width.

        height: is a private instance attribute,
        represents the rectangle's height.

        x: is a private instance attribute.

        y: is a private instance attribute.

        id: is a public instance attribute from
        super class Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This is the class constructor method.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """
        Method that returns the rectangle's width.
        """
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Method that returns the rectangle's height.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Method to set the value of height.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        Method to retrieve x.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Method to set the value of x.
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):
        """
        Method that retrieves y.
        """
        return self.__y
    @y.setter
    def y(self, y):
        """
        Method that sets y's value.
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be > 0")
        self.__y = y

    def area(self):
        """
        Public method that returns the are of that
        returns the Rectangle's area.
        """
        area = self.__height * self.__width
        return area

    def display(self):
        """
        Public method that print in stdout the Rectangle
        instance with '#'.
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        print_symbol = '#'
        for row in range(self.__height):
            for column in range(self.__width):
                string += str(print_symbol)
                if row < self.__height - 1:
                    string += '\n'
        return string
