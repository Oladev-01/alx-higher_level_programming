#!/usr/bin/python3
""" This module defines a class of square """


class Square:
    """ This class defines an object of Square and returns the area
     based on the size """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def __eq__(self, comp):
        return self.area() == comp.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __le__(self, comp):
        return self.area() <= comp.area()

    def __gt__(self, comp):
        return self.area() > comp.area()

    def __lt__(self, comp):
        return self.area() < comp.area()

    def __ne__(self, comp):
        return self.area() != comp.area()
