#!/usr/bin/python3
"""
This module defines a function is_same_class.
"""


def is_same_class(obj, a_class):
    """
    This function returns True if the object is exactly an instance of
    the specified class ; otherwise False.
    """

    if type(obj) is a_class:
        return (True)
    else:
        return (False)
