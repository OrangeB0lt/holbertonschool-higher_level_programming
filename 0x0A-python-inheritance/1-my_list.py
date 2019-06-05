#!/usr/bin/python3
"""
mod 1-my_list contains class MyList
"""


class MyList(list):
    """ define Mylist Class """

    def __init__(self):
        """ init the object """
        super().__init__()

    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))
