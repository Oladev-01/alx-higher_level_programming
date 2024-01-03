#!/usr/bin/python3
""" This module defines a class of square """


class Square:
    """ This class defines a class of square and returns the area of the object
    based on the size """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self, value):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if all(isinstance(i, int) and i >= 0 for i in value):
                self.__position = value
            else:
                raise TypeError("position must be a tuple"
                                " of 2 positive integers")
        else:
            raise TypeError("position must be a"
                            " tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
