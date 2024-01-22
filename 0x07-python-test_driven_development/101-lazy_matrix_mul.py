#!/usr/bin/python3
import numpy as np
"""This module defines a function that multiplies
 each element of two matrices"""


def lazy_matrix_mul(m_a, m_b):
    """This function calculates the scalar product of two matrices"""

    # Validate m_a and m_b
    if not m_a or not any(m_a):
        raise ValueError("m_a must not be empty")

    if not m_b or not any(m_b):
        raise ValueError("m_b must not be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if any(not all(isinstance(el_1, (int, float))
                   for el_1 in row) for row in m_a):
        raise TypeError("m_a should only contain only integers or floats")

    if any(not all(isinstance(el, (int, float)) for el in row) for row in m_b):
        raise TypeError("m_b should only contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    np_a = np.array(m_a)
    np_b = np.array(m_b)

    result = np.dot(np_a, np_b)
    result_list = result.tolist()

    return result_list
