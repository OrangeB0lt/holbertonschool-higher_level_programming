#!/usr/bin/python3
"""
contains load_from_json_file funct
"""
import json


def load_from_json_file(filename):
    """creates obj from json file"""
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
