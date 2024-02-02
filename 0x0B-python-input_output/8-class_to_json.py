#!/usr/bin/python3
"""this module defines a function that retuns a
dictionary representation for JSON serialization of
an object"""


def class_to_json(obj):
    """retuns dictionary repr of obj"""
    if hasattr(obj, '__dict__'):
        data_dict = {}
        for key, value in obj.__dict__.items():
            if isinstance(value, (int, list, dict, bool, str)):
                data_dict[key] = value
            elif hasattr(value, '__dict__'):
                data_dict[key] = class_to_json(value)
    return data_dict
