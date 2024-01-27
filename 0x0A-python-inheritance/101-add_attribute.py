#!/usr/bin/python3
"""This module defines a program that adds a new attr
bute to a class"""


def add_attribute(obj, name, value):
    """
    This function adds a new attribute to an object:
    obj : the object to add a new attribute
    name: the name of the attribute
    value: the value (attribute value) to be added to the object
    """

    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
