#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    new_matrix = [[x**2 for x in m] for m in new_matrix]
    return new_matrix
