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
        if x < 0:
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
        print('\n' * self.__y, end='')
        for row in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self):
        """
        This is a method that returns a human-readable string,
        that is a representation of the object.
        It generates output for end user.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """
        This is a public method that assigns an argument to each
        attribute.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Public method that returns the dictionary representation
        of a Rectangle.
        """
        rdict = {}
        rdict[id]