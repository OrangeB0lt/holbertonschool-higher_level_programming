#!/usr/bin/python3
def no_c(my_string):
    no_c_string = []
    for index in my_string:
        if index != 'c' and index != 'C':
            no_c_string.append(index)
    return "".join(no_c_string)
