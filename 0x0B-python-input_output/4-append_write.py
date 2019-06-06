#!/usr/bin/python3
"""
contains the funct append_write
"""


def append_write(filename="", text=""):
    """returns num of chars appended to file from text"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
