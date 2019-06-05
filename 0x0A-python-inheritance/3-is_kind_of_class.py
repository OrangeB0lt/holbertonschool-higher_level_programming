#!/usr/bin/python3
"""
contains is_kind of class funct
"""


def is_kind_of_class(obj, a_class):
    """ True if obj is an instance or inher from a_class """
    return isinstance(obj, a_class)
