#!/usr/bin/python3
""" This module defines a class of square """


class Square:
    """ This class defines a sqaure of variable sizes """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

if __name__ == "__main__":
    import doctest
    doctest.testfile('2-main.py')
