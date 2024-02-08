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

        number_of_instances: is a public class attribute which counts
        the number of Rectangle instances.

        print_symbol: is a public class attribute used as the symbol
        for string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """
        This is a method that returns a human-readable string,
        that is a representation of the object.
        It generates output for end user.
        """

        string = ""
        if self.__width == 0 or self.__height == 0:
            return (string)

        print_symbol = getattr(self, 'print_symbol', self.print_symbol)

        for row in range(self.__height):
            for column in range(self.__width):
                string += str(print_symbol)
            if row < self.__height - 1:
                string += '\n'

        return (string)

    def __repr__(self):
        """
        This is a method that returns a string representation of the object.
        It generates output for developer.
        """

        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """
        This is a method to delete an instance of Reactangle.
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        This is a static method which compares two rectangles and
        returns the biggest one.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return (rect_1)
        elif rect_1.area() == rect_2.area():
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        """
        This is a class method which returns a new Rectangle instance
        with the same size of width and height.
        """
        return (Rectangle(size, size))
