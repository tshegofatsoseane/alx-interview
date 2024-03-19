#!/usr/bin/python3
""" Computes the minimum operations
    needed in a CopyAll - Paste task
"""


def minOperations(n):
    """
    Method to compute the minimum number
    of operations for task Copy All and Paste

    Args:
        n: input value
        factor_list: List to save the operations
    Return: sum of all operations
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
