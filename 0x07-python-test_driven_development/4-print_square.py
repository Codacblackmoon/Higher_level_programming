#!/usr/bin/python3
"""
Module text_indentation
text_indentation
"""


def print_square(size):
    """
    Print a square
    """
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be a non-negative integer')
    if size == 0:
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
