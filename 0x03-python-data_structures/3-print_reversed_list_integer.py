#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        pass
    else:
        for index in reversed(range (0, len(my_list))):
            print("{:d}" .format(my_list[index]))
