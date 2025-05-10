#!/usr/bin/python3
"""
Module that calculates the fewest number of operations
needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result
    in exactly n H characters in the file
    Args:
        n: number of H characters to achieve
    Returns:
        Integer: minimum number of operations needed
        If n is impossible to achieve, return 0
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

        # If divisor exceeds n, then n is prime
        if divisor > n:
            if n > 1:
                operations += n
            break   
    return operations
