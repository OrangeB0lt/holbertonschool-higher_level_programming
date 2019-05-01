#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if ord('a') <= ord(character) <= ord('z'):
            character = chr(ord(character) + (ord('A') - ord('a')))
        print("{:s}" .format(character), end="")
    print("")
