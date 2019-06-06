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

    def to_json(self, attrs=None):
        """grabs dict representation of student instance"""
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        for att in attrs:
            if type(att) is not str:
                return self.__dict__
        return {i: self.__dict__[i] for i in self.__dict__ if i in attrs}
