#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    arguments = len(argv)
    if arguments is not 4:
        print("Usage:", argv[0], '<a> <operator> <b>')
        exit(1)

    num1 = int(argv[1])
    operator = argv[2]
    num2 = int(argv[3])

    if operator is '+':
        numE = add(num1, num2)

    elif operator is '-':
        numE = sub(num1, num2)

    elif operator is '*':
        numE = mul(num1, num2)

    elif operator is '/':
        numE = div(num1, num2)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {} {:d} = {:d}" .format(num1, operator, num2, numE))
