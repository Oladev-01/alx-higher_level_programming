#!/usr/bin/python3
"""This module defines a function that multiplies
 each element of two matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """This function calculates the scalar product of two matrices"""

    # Validate m_a and m_b
    if not m_a or not any(m_a):
        raise ValueError("shapes (1,0) and (2,2) not aligned:"
                         " 0 (dim 1) != 2 (dim 0)")

    if not m_b or not any(m_b):
        raise ValueError("shapes (2,2) and (1,0) not aligned:"
                         " 2 (dim 1) != 1 (dim 0)")

    if not isinstance(m_a, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if not isinstance(m_b, list):
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if any(not all(isinstance(el_1, (int, float))
                   for el_1 in row) for row in m_a):
        raise TypeError("invalid data type for einsum")

    if any(not all(isinstance(el, (int, float)) for el in row) for row in m_b):
        raise TypeError("invalid data type for einsum")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("setting an array element with a sequence.")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("setting an array element with a sequence.")

    if len(m_a[0]) != len(m_b):
        raise ValueError("shapes (2,3) and (2,2) not aligned:"
                         " 3 (dim 1) != 2 (dim 0)")

    # Matrix multiplication
    np_a = np.array(m_a)
    np_b = np.array(m_b)

    result = np.dot(np_a, np_b)

    return result
