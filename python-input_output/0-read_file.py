#!/usr/bin/python3
"""
This module defines a function that read_file.
"""


def read_file(filename=""):
    """
    This function reads a text file and prints it to stdout.
    """

    with open(filename, "r") as file:
        print(file.read().rstrip("\n"))
