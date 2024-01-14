#!/usr/bin/python3
""" This module the string My name is
 <first name> <last name>. the first name and 
 last name represent name of a person and must 
 be a string"""


def say_my_name(first_name, last_name=""):
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")

