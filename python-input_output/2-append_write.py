#!/usr/bin/python3
"""
This module defines a function called append_write.
"""


def append_write(filename="", text=""):
    """
    This function appends a string at the end of a text file
    and returns the number of characters added.
    """

    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
