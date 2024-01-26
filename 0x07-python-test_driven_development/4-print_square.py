#!/usr/bin/python3
"""
Module for the  print_square function
Prints a square with the character #.
"""


def print_square(size):
    """Prints a square with size which is
    the length and width of the square.
    """

    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is than 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Check if size is a float and is less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Print the square
    for i in range(size):
        print("#" * size)
