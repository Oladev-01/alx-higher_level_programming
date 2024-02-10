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
        first_elem = list_dictionaries[0]
        if isinstance(first_elem, dict):
            return json.dumps(list_dictionaries)
        else:
            return json.dumps([obj.to_dictionary()
                               for obj in list_dictionaries])

    @staticmethod
    def from_json_string(json_string):
        """this method load from a json string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        """this method creates a new instance of the class with
        attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_inst = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_inst = cls(1)
        dummy_inst.update(**dictionary)
        return dummy_inst
