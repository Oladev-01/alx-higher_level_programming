#!/usr/bin/python3
"""pascal's triangle"""
from math import factorial

def pascal(n):
   """the code begins"""
   for rows in range(n): # the rows of the triangle
        for space in range(1, n - rows): # creating even triangle, using the space as padding
         print(end=' ') # print the padded spaces
        for column in range(rows + 1): # the column
           pascal_tr = factorial(rows) // (factorial(column) * factorial(rows - column))
           print(pascal_tr, end=' ')
        print() # marks a new line to the next row
        # we have come to the end of the code, let's run.....!!!

pascal(8)


# thank you for watching
