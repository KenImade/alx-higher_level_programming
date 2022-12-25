#!/usr/bin/python3
"""
This module defines `print_square`

The function prints a square made with the character #
"""


def print_square(size):
    """
    prints a square made with the character #

    Args:
        size: integer

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0

    Returns:
        Nothing
    """

    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print('#' * size)
