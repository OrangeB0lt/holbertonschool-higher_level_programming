#!/usr/bin/python3
"""
Contains pascal_triangle funct
"""


def pascal_triangle(n):
    """returns pascal triangle of n"""
    if n <= 0:
        return []
    p_t = [[] for i in range(n)]
    p_t[0] = [1]
    if n > 1:
        p_t[1] = [1, 1]
    if n > 2:
        for c in range(2, n):
            p_t[c].append(1)
            for q in range(c - 1):
                p_t[c].append(p_t[c - 1][q] + p_t[c - 1][q + 1])
            p_t[c].append(1)
    return p_t
