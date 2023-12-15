#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first and second elements from both tuples
    a = []
    b = []
    for i in range(len(tuple_a)):
        if not tuple_a[i]:
            a[i] = 0
        else:
            a[i] = tuple_a[i]
    for m in range(len(tuple_b))
        if not tuple_b[m]:
            b[m] = 0
        else:
            b[m] = tuple_b[m]
    result = (a[0] + b[0], a[1] + b[1])
    return result
