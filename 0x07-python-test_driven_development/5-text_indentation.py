#!/usr/bin/python3
"""this module defines a function that prints a string addding two
 newline after the occurence of . : and ?"""


def text_indentation(text):
    """this function prints a string addding two newline after the
    occurence of . : and ?"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    mod_string = ""
    inst = {'.', '?', ':'}
    newline = False

    for i in text:
        if newline and i.isspace():
            continue
        mod_string += i
        if i in inst:
            mod_string += '\n\n'
            newline = True
        else:
            newline = False

    print(mod_string.rstrip())
