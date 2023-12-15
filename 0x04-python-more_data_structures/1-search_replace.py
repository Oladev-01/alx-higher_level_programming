#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    else:
        new_list = my_list[:]
        for i in range(len(my_list)):
            if new_list[i] == search:
                new_list[i] = replace
        return new_list
