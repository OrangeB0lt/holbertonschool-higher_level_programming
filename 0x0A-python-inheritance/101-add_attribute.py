#!/usr/bin/python3
"""
mod 101-add_attribute contains funct of same name
"""


def add_attribute(obj, name, value):
    """ if possible, adds new attribute to an obj """
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can\'t add new attribute")
