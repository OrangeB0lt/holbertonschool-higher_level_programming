#!/usr/bin/python3
"""
   Class module for Rectangle 
"""

class Rectangle:
    """
    Class attributes
    height
    width
    area
    perimeter
    both have setter and property defs
    """
    number_of_instances = 0    

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        width = '#' * self.width
        rectangle = width
        for idx in range(self.height - 1):
            rectangle += "\n" + width
        return (rectangle)
    
    def __repr__(self):
        return("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """<WIDTH> * <HEIGHT> = <AREA>
        """
        return self.width * self.height
    
    def perimeter(self):
        """2 * (<WIDTH> + <HEIGHT>)
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)