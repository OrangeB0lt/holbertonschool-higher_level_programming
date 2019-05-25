#!/usr/bin/python3
"""
    Prints squares
    based on size input
    woohoo
"""
def print_square(size):
    """
        print_square: prints a square based on input number for size
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for idx in range(size):
        for cnt in range(size):
            print("#", end="")
        print()