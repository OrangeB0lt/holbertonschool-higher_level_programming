#!/usr/bin/python3
"""
contains class Student
"""


class Student:
    """define class Student"""

    def __init__(self, first_name, last_name, age):
        """inits new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """grabs dict representation of student instance"""
        return self.__dict__
