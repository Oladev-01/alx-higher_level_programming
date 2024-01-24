#!/usr/bin/python3
"""this module defines a class that prints a
sorted list"""


class MyList(list):
    """this class inherits a list and defines a function
    that prints a sorted list"""

    def print_sorted(self):
        print(sorted(self))
