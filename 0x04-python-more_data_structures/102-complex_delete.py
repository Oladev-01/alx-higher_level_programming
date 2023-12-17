#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None or not a_dictionary:
        return None
    str = []
    for i, j in a_dictionary.items():
        if j == value:
            str.append(i)
    for key in str:
        del a_dictionary[key]
