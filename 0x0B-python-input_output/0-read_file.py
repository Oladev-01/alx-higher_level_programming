#!/usr/bin/python3
"""This module defines a function that reads a text file
with encoding UTF-8"""


def read_file(filename=""):
    """Reads a text file (UTF-8) and prints it to stdout"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
