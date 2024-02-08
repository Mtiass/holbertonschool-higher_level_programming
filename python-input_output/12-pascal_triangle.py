#!/usr/bin/python3
"""
This module defines pascal_triangle as a function.
"""


def pascal_triangle(n):
    """
    This is a function that returns a list of lists of integers
    representing the Pascal’s triangle of n.
    """

    listt = []
    if n <= 0:
        return (listt)
    else:
        for i in range(n):
            rowlist = []
            elem = 1

            for con in range(i + 1):
                rowlist.append(elem)
                elem = elem * (i - con) // (con + 1)

            listt.append(rowlist)
    return (listt)
