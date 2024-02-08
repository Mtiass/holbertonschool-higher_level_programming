#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list.
"""


class MyList(list):
    """
    This is a class that defines a list.
    """

    def print_sorted(self):
        """
        This is a public instance method that prints the list,
        but sorted (ascending sort).
        """

        print(sorted(self))
