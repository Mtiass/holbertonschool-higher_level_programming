#!/usr/bin/python3
"""
This module defines the class Square that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This is a class that defines Square, that inherits from Rectangle
    
    Attributes:
        width: is a private instance attribute,
        represents the square's size.

        height: is a private instance attribute,
        represents the square's size.

        x: is a private instance attribute.

        y: is a private instance attribute.

        id: is a public instance attribute from
        super class Base.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This is the class constructor method.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Method that returns the size of the square.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Method that sets the square size.
        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def __str__(self):
        """
        This is a method that returns a human-readable string,
        that is a representation of the object.
        """
        return ("[Square] ({}) {}/{} - {}".format(
           self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """
        This is a public method that assigns an argument to each
        attribute.
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Public method that returns the dictionary representation
        of a Rectangle.
        """
        rdict = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
            }
        return rdict
