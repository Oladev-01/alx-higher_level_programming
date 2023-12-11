#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for i in mat:
            print("{:d}".format(i), end=' ')
        print()
