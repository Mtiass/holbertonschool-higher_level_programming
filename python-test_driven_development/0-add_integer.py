#!/usr/bin/python3
"""
Module that defines a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Function to add two integers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
