#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if not isinstance(value, int):
            raise TypeError
        else:
            print("{:d}".format(value))
    except TypeError:
        return False
    return True
