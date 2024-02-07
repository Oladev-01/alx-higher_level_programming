#!/usr/bin/python3
"""this module defines a class Rectangle that inherits
from class Base"""
from models.base import Base


class Rectangle(Base):
    """this is a class Rectange"""
    def __init__(self, width, height, x=0, y=0, id=None):
        (self.width, self.height, self.x, self.y) = (width, height, x, y)
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        self.__width = width

    @width.setter
    def height(self, height):
        self.__height = height

    @width.setter
    def x(self, x):
        self.__width = x

    @width.setter
    def y(self, y):
        self.__y = y
