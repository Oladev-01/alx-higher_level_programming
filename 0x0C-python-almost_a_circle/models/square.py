#!/usr/bin/python3
"""this module defines a class square that
inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class of square that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        string = (f"[Square] ({self.id}) {self.x}/{self.y}"
                  f" - {self.width}")
        return string
