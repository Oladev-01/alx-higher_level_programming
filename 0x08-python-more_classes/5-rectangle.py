#!/usr/bin/python3
""" this module defines a class of rectangle"""


class Rectangle:
    """ This class defines an object of rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if (self.__width == 0 or
                self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if (self.__width == 0 or
                self.__height == 0):
            return ""
        string = ""
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            string += "\n"
        return string.rstrip("\n")

    def __repr__(self):
        return f"Rectangle ({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
