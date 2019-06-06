#!/usr/bin/python3
"""
contains save_to_json_file funct
"""
import json


def save_to_json_file(my_obj, filename):
    """writes obj to txt file using json"""
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
