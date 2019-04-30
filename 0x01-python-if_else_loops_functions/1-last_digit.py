#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    rand = number % 10
else:
    rand = number % -10

print('Last digit of {:d} id {:d}' .format(number,rand), end=" ")

if rand == 0:
    print('and is 0')
elif rand < 6 or number < 0:
    print('and is less than 6 and not 0')
else:
    print('and is greater than 5')
