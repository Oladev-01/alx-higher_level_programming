#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list or my_list is None:
        return None
    size = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end='')
            size += 1
    except IndexError:
        pass
    finally:
        print()
    return size
