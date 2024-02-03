#!/usr/bin/python3
"""this module defines a function that returns
pascal triangle representation of a number """


def pascal_triangle(n):
    """this fucntion returns the pascal triangle repr of a
    number"""
    if n < 0:
        return []
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
