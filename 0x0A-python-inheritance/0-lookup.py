#!/usr/bin/python3
"""this module defines a function that returns the list
of available attributes and methods of an object"""


def lookup(obj):
    """this function returns all attributes and methods of an object
    as a list"""

    return [meth_att for meth_att in dir(obj)]
