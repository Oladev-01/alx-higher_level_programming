#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    num = len(my_list)
    if num == 0:
        return None
    else:
        for i in range(num - 1, -1, -1):
            print("{:d}".format(my_list[i]))
