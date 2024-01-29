#!/usr/bin/python3
"""This module defines a function that reads a text file
with encoding UTF-8"""


def read_file(filename=""):
    """This function opens and read from a file of
    encoding UTF-8"""
    if not filename:
        print("")
    with open(filename, 'r', encoding="utf-8") as file:
        opened_file = file.read()
    opened_file.rstrip("\n")
    print(opened_file)