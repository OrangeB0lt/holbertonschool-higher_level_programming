#!/usr/bin/python3
"""
mod 4-inherits_from contains funct inherits_from
"""


def inherits_from(obj, a_class):
    """ returns True if obj is a subclass of a_class """
    return issubclass(type(obj), a_class) and type(obj) != a_class