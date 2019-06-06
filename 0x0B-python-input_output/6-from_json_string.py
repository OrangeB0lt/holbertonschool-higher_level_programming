#!/usr/bin/python3
"""
contains from_json_string function
"""
import json


def from_json_string(my_str):
    """returns obj rep by json string"""
    return json.loads(my_str)
