#!/usr/bin/python3
for character in range(97, 123):
    if character is 113 or character is 101:
        continue
    else:
        print("{}" .format(chr(character)), end="")
