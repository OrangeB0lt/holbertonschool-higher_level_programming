#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    length = len(argv)
    print('{:d} argument{:}' .format(length - 1, '.' if length == 1
                                     else (':' if length == 2 else 's:')))
    index = 1
    for argument in argv[1:]:
        print('{:d}: {}' .format(index, argument))
        index += 1
