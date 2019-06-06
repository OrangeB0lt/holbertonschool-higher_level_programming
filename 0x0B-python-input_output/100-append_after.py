#!/usr/bin/python3
"""
contains append_after funct
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text after each line containing a string"""
    with open(filename, 'r+', encoding='utf-8') as f:
        inp = []
        for outp in f:
            inp.append(outp)
            if search_string in outp:
                inp.append(new_string)
        f.seek(0)
        for outp in inp:
            f.write(outp)
