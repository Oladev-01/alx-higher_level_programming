#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3.9],
    [3, 4, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)

matrix = [
    [1, 2, 3],
    [3, 4, 6]
]
print(matrix_divided(matrix,[3]))
print(matrix)
