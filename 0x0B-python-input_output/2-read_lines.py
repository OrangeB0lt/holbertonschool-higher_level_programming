#!/usr/bin/python3
"""
contains read_line function
"""


def read_lines(filename="", nb_lines=0):
    """reads n lines in a file, prints to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
            return
        idx = 0
        for idx, line in enumberate(f):
            if idx == nb_lines:
                break
            print(line, end='')
