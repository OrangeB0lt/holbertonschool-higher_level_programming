#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    print('{}' .format(sum(int(num) for num in argv[1:])))
