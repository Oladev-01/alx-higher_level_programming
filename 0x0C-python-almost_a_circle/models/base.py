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
            return "[]"
        return json.dumps([obj.to_dictionary() for obj in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """this method writes a json representation of
        the class to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        args = cls.to_json_string(list_objs)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(args)
