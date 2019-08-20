#!/usr/bin/python3
''' function to find_peaks '''


def find_peak(list_of_integers):
    ''' finds peak in list of unsorted integers '''
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    Lf = 0
    Rt = len(list_of_integers) - 1
    return helper(list_of_integers, Lf, Rt)

def helper(list, left, right):
    ''' finds peak through recursion binary search '''
    if left == right:
        return(list[right])
    middle = (right + left) // 2
    if list[middle] > list[middle + 1]:
        return helper(list, left, middle)
    return helper(list, middle + 1, right)
