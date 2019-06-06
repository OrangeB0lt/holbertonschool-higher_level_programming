#!/usr/bin/python3
"""
contains write_file function
"""

def write_file(filename="", text=""):
    """writes a string to file and return num of chars written"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
