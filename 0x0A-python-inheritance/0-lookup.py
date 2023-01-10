#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """return list of attributes and methods of object

    Args:
        obj (Any): object

    Returns:
        list: list of object attributes
    """

    return dir(obj)
