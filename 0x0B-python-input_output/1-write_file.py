#!/usr/bin/python3
"""this module defines a funcion that writes a string
to a text file in encoding utf-8"""


def write_file(filename="", text=""):
    """this function writes to a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        num_char = file.write(text)
    return num_char
