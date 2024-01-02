#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        sys.stdout.write("{:d}\n".format(int(value)))
        return True
    except ValueError:
        sys.stderr.write("Exception: {}\n".format(sys.exc_info()[1]))
        return False
