#!/usr/bin/python3
"""this module defines a class which inherits
 from class Int"""


class MyInt(int):
    def __eq__(self, value):
        return not super().__eq__(value)

    def __ne__(self, value):
        return not super().__ne__(value)
