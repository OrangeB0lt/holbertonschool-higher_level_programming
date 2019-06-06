#!/usr/bin/python3
"""
contains class_to_json funct
"""


def class_to_json(obj):
    """return dict desc for json obj"""
    return obj.__dict__
