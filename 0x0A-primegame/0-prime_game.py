#!/usr/bin/python3
"""Module for Prime Game"""


def isWinner(x, nums):
    """
    Determine the winner in a set of prime numbers.

    Args:
        x (int): No. of rounds.
        nums (list of int): Integer list

    Returns:
        str: Best player's name
        None: If no winner.

    Raises:
        None.
    """
    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None
    ben = 0
    maria = 0
    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)
    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # Determine the winner of the game
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
    Delete multiples of prime number from array.

    Args:
        ls (list of int): Array of prime numbers.
        x (int): Target prime number.

    Returns:
        None.

    Raises:
        None.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
