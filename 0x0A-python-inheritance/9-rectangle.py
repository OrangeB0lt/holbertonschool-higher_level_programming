#!/usr/bin/python3
"""
contains class BaseGeometry and subclass Rectangle
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

class Rectangle(BaseGeometry):
    """ A repre of a rectangle """
    def __init__(self, width, height):
        """ instantiation of rectangle """
        self. integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returns area of rect """
        return self.__width * self.__height

    def __str__(self):
        """ informat string of rep of the rect """
        return "[Rectangle] {:d}/{:d}" .format(self.__width, self.__height)
