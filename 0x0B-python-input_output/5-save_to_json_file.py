#!/usr/bin/python3
"""This module defines a function that writes the JSON
representation of an object to a string"""
import json


def save_to_json_file(my_obj, filename):
    """This module defines a function that returns the JSON rep
    of a string"""
    with open(filename, 'w', encoding='utd-8') as file:
        json.dump(my_obj, file)
