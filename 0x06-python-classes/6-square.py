#!/usr/bin/python3
"""
Square Class def
"""

class Square:
    """
    Square class with priv instance att size
    """

    def __init__(self, size=0):
        """
        Args:
          size: size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        size: size of the square
        setter validates size is an int and >= 0

        Raise:
            TypeError and ValueError
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        size: size of the square
        setter validates size is an int and >= 0

        Raise:
            TypeError and ValueError
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        prints to the stdout square with # or empty line if 0
        """
        print("\n".join(["".join(["#" for a in range(slef.__size)])
                         for b in range(self.size)]))

    def area(self):
        """
        Returns area of the square instance
        """
        return (self.__size ** 2)

    def _tuple_(self, position):
        """
        check if it is a tuple and integer
        """
        if type(position is not tuple or len(position) != 2:
            return False
        elif type(position[1]) is not int or position[1] < 0:
            return False
        elif type(position[0]) is not int or position[0] < 0:
            return False
        else:
            return True
