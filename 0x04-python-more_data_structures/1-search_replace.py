#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newL = []
    for index in my_list:
        if index != search:
            newL.append(index)
        else:
            newL.append(replace)
    return newL
