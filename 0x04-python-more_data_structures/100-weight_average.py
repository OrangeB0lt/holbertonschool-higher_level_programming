#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) and my_list:
        number = 0
        count = 0
        for toittups in my_list:
            number += (toittups[0] * toittups[1])
            count += toittups [1]
        return (number / count)
    else:
        return 0
