#!/usr/bin/python3
"""
This module defines a function called write_file.
"""


def write_file(filename="", text=""):
    """
    This function writes a string to a text file and returns
    the number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)

    return(len(text))
