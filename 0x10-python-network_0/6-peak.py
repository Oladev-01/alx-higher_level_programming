#!/usr/bin/python3
"""this module defines a function that identifies
 the peak within a list of numbers"""


def find_peak(list_of_integers):
    """this function finds a peak within list of numbers"""
    arr = list_of_integers
    if arr is None or len(arr) == 0:
        return None
    n = len(arr)
    if n == 1:
        return arr[0]
    left, right = 0, n - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return arr[left]
