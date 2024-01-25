#!/usr/bin/python3
"""This module defines a function that checks
if an object is an instance of a class"""


def inherits_from(obj, a_class):
    """This function checks if an object is an instance of a class"""

    if not isinstance(obj, a_class):
        return False
    else:
        return True

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))