#!/usr/bin/python3
"""This module defines a rectangle class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a rectangle class"""

    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("{}", height.format(height))
        self.integer_validator("{}", width.format(width))
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
