#!/usr/bin/python3
"""This module defines a function that returns the
object represented by JSON"""
import json


def from_json_string(my_str):
    """this function returns the object represented by JSON"""
    return json.loads(my_str)
