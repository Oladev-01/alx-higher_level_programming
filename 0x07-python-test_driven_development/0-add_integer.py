#!/usr/bin/python3
""" This module. add_integer adds two integers and returns the
result of the addition. the two integers must be of int or
float value, else TypeError is raised. also the two integers
would be casted into int before it returns the addition
of the values. """


def add_integer(a, b=98):
    """ This function adds two integers and returns
    the value as int. float values are first converted to int
    before the addition"""

    if a != a and b != b:
        raise ValueError
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
