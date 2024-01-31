#!/usr/bin/python3
"""This module defines that extract a JSON representation of
an object from a file"""
import json


def load_from_json_file(filename):
    """this function creates a JSON representaton of an
    object from a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        extract = json.load(file)
        return extract
