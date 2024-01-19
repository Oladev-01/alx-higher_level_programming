#!/usr/bin/python3
""" This module defines a function of matrix that divides
each element of the matrix by div which is the second argument
the matrix must be an integer """


def check_matrix(matrix_1):
    """ This function checks if the list is valid. i.e
    the arguments passed is a list of list of integers or float
    """

    if not all(isinstance(row, list) for row in matrix_1):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")

    row_size = set(len(row) for row in matrix_1)
    if len(row_size) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not (all(isinstance(item, (int, float))
                for row in matrix_1 for item in row)):
        raise TypeError("matrix must be a matrix"
                        " (list of lists) of integers/floats")

    return matrix_1


def matrix_divided(matrix, div):
    """ this function divides a matrix by the second argunment
    and the values of each division is rounded off to 2 d.p"""

    checked_matrix = check_matrix(matrix)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = checked_matrix
    new_matrix = [[round(item / div, 2) for item in row] for row in new_matrix]
    return new_matrix
