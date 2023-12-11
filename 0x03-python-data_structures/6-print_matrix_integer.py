#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for i in range(len(mat)):
            if i != 0:
                print(" ", end='')
            print("{:d}".format(mat[i]), end='')
        print()
