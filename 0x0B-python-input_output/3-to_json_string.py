#!/usr/bin/python3
"""This module defines a function that returns the JSON
representation of a string"""
import json


def to_json_string(my_obj):
    """This module defines a function that returns the JSON rep
    of a string"""
    return json.dumps(my_obj)
