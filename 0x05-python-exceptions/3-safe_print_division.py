#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if not a or not b:
            raise ValueError
        elif b == 0:
            raise ZeroDivisionError
        else:
            c = a / b
    except (ValueError, ZeroDivisionError):
        c = None
    finally:
        print("Inside result: {}".format(c))
        return c
