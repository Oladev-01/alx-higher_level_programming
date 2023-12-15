#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None
    else:
        a = 0
        for i in set(my_list):
            a += int(i)
        return a
