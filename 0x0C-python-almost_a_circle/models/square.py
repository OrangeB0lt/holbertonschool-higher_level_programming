#!/usr/bin/python3
"""
Class for square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def to_dictionary(self):
        """
        returns dict repr of square
        """
        return {
            'id': self.id, 'size': self.size,
            'x': self.x, 'y': self.y
        }
    
    def update(self, *args, **kwargs):
        """
        assigns attri to square
        """
        storedArr = ["id", "size", "x", "y"]
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
        for idx, arg in enumerate(args):
            setattr(self, storedArr[idx], arg)

