#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is 0:
        return None
    else:
        number = my_list[0]
        for index in my_list:
            if index > number:
                number = index
    return number
