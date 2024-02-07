#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.width)

    r2 = Rectangle(2, 13)
    print(r2.height)

    r3 = Rectangle(10, 2, 0, 5, 12)
    print(r3.y)