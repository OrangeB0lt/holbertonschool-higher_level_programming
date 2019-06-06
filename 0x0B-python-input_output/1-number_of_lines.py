#!/usr/bin/python3
"""
Contains number_of_lines function
"""


def number_of_lines(filename=""):
    """returns number of lines in a text file"""
    with open(filename, encoding='utf8') as f:
        for line in f:
            count += 1
    return count
