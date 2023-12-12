#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or not my_list:
        return None
    else:
        a = 0
        for i in my_list:
            if i > a:
                a = i
        return a
