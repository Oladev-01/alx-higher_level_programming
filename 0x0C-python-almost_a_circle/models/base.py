#!/usr/bin/python3
"""this module defines a base class of all
other classes in this project"""


class Base:
    """this is the base class of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
