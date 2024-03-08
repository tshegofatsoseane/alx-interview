#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

def pascal_triangle(n):
    """Creates a new function def pascal_triangle(n): which returns a list of lists
    with integers representing Pascal's triangle
    """

    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
