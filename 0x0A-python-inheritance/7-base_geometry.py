#!/usr/bin/python3
"""
contains class BaseGeometry
"""


class BaseGeometry:
    """ Class with pub attri area """
    def area(self):
        """ raises an except when called """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value if positive """
        if type(value) is not int:
            raise TypeError("{} must be an integer" .format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0" .format(name))