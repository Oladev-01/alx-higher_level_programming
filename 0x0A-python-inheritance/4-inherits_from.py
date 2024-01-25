#!/usr/bin/python3
"""This module defines a function that checks
if an object is an instance of a class"""


def inherits_from(obj, a_class):
    """This function checks if an object is an instance of a class"""

    return issubclass(type(obj), a_class)
