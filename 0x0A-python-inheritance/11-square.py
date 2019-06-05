#!/usr/bin/python3
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

class Square(Rectangle):
    """ A representation of square """
    def __init__(self, size):
        """ instantiation of square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ returns area of square """
        return self.__size ** 2

    def __str__(self):
        """ informat string rep of square """
        return "[Square] {:d}/{:d}" .format(self.__size, self.__size)