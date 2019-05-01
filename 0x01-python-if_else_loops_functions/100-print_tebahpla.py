#!/usr/bin/python3
for letter in reversed(range(ord('a'), ord('z') + 1)):
    if letter % 2 != 0:
        letter = letter - 32
    print('{:c}' .format(letter), end="")
