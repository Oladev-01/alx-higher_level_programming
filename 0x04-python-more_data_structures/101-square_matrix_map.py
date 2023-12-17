#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return [list(map(lambda y: pow(y, 2), j)) for j in matrix[:]]
