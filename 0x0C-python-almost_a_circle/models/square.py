#!/usr/bin/python3
"""this module defines a class square that
inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class of square that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """this method updates the value of the class"""
        keys = ['id', 'size', 'x', 'y']
        if args:
            for key, value in enumerate(args):
                setattr(self, keys[key], value)
        if kwargs:
            for key, value in kwargs.items():
                if key in keys:
                    setattr(self, key, value)

    def to_dictionary(self):
        """this method returns the dictionary representation of the class"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        string = (f"[Square] ({self.id}) {self.x}/{self.y}"
                  f" - {self.width}")
        return string
