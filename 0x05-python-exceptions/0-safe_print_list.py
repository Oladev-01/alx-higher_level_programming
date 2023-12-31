#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
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
