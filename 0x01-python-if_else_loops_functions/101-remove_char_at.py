#!/usr/bin/python3
def remove_char_at(str, n):
    index = 0
    nexxt = ""
    for character in str:
        if index != n:
            nexxt += character
        index += 1
    return (nexxt)
