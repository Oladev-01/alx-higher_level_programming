#!/usr/bin/python3
"""This module defines a function that checks
if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """This function checks if an object is an instance of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
