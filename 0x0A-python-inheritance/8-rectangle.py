#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""This module defines a rectangle class"""


class Rectangle(BaseGeometry):
    """a rectangle class"""

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("height", height)
        self.integer_validator("width", width)
        self.__width = width
        self.__height = height
