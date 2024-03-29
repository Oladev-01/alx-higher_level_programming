#!/usr/bin/python3
"""This module defines a squatre class that
inherits from a rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a class of square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
