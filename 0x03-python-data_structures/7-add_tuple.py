#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    tup_a = tuple_a + (0, 0)
    tup_b = tuple_b + (0, 0)
    tup_a = tup_a[0:2]
    tup_b = tup_b[0:2]

    return tuple(map(sum,zip(tup_a, tup_b)))
