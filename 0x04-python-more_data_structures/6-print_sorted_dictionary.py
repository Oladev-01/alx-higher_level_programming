#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return None
    for i, j in sorted(a_dictionary.items()):
        print("{}: {}".format(i, j))
