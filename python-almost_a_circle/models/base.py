#!/usr/bin/python3
"""
This module defines Base as a class.
"""


class Base:
    """
    This is a class that works as a base for other classes.

    Attributes:
        nb_objects: is a private class attribute.

        id: is a public instance attribute.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        This is the initialization method.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
