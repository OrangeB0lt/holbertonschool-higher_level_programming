#!/usr/bin/python3
"""
contains the read_file function
"""

def read_file(filename=""):
    """ reads text file, prints to stdout """
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end="")
