#!/usr/bin/python3
""" This module defines a class of squares """


class Square:
    """ this class defines a square and returns its area """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if isinstance(value, tuple):
            if all(isinstance(i, int) and i >= 0 for i in value):
                self.__position = value
            else:
                raise TypeError("position must be a tuple"
                                " of 2 positive integer")
        else:
            raise TypeError("position must be a tuple of 2 positive integer")

    def area(self):
        return self.__size ** 2

    def __str__(self):
        if self.__size == 0:
            return ""

        string = ""
        for i in range(self.__position[1]):
            string += "\n"
        for i in range(self.__size):
            string += " " * self.__position[0] + "#" * self.__size + "\n"
        return string.rstrip("\n")
