#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nu_lyst = list(my_list)
    if idx < 0 or idx > len(my_list) - 1:
        return nu_lyst
    else:
        nu_lyst[idx] = element
        return nu_lyst
