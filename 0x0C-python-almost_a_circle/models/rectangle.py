#!/usr/bin/python3
"""
Module contains class Rectangle
"""

from models.base import Base


class Rectangle(Base):
    """
        rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self. y, self.width, self.height)
    
    def area(self):
        """
            returns area
        """
        return self.width * self.height
    
    def display(self):
        """
            prints the rectangle
        """
        print("\n" * self.y, end="")
        for idx in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)
    
    def to_dictionary(self):
        """
        Returns dict repr of rectangle
        """
        return {
            'id': self.id, 'width' : self.width,
            'height': self.height, 'x': self.x,
            'y': self.y
        }
    
    def update(self, *args, **kwargs):
        """
        updates rectangle
        """
        storedArr = ["id", "width", "height", "x", "y"]
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for idx, arg in enumerate(args):
            setattr(self, storedArr[idx], arg)

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError ("y myst be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val
