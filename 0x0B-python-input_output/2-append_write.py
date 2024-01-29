#!/usr/bin/python3
"""This module defines a function that appends a string
at the end of a text file and returns the number of
 characters added. encoding is utf-8"""


def append_write(filename="", text=""):
    """this function appends a string to a text file"""
    with open(filename, 'a', encoding='utf-8') as file:
        num_char = file.write(text)
        return num_char
