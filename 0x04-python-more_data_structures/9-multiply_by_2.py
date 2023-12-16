#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    new_dictionary = a_dictionary.copy()
    for x in new_dictionary:
        new_dictionary[x] *= 2
    return new_dictionary
