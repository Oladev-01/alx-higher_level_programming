#!/usr/bin/python3
"""This module defines a function that adds a new
string to the file after the occurrrence of a search string"""


def append_after(filename="", search_string="", new_string=""):
    """this function adds a new string to a file
    after the occurrence of a search string"""
    with open(filename, 'r', encoding='utf-8') as file:
        each_lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for lines in each_lines:
            file.write(lines)
            if search_string in lines:
                file.write(new_string)
