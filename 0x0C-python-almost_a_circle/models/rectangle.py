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

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """this method retuns the area of the class
        rectangle"""
        return self.__height * self.__width

    def display(self):
        """this method prints the area of the rectangle as #"""
        for row in range(self.__height):
            for column in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        string = (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                  f" - {self.__width}/{self.__height}")
        return string
