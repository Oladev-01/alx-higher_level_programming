#!/usr/bin/python3
"""this module defines a base class of all
other classes in this project"""
import json


class Base:
    """this is the base class of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or not list_dictionaries:
            return []
        return json.dumps(list_dictionaries)
