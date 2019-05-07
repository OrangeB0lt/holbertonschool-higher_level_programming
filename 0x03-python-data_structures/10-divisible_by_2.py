#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bi_list = []
    for index in my_list:
        if index % 2 != 0:
            bi_list.append(False)
        else:
            bi_list.append(True)
    return bi_list
