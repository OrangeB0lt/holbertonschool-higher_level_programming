#!/usr/bin/python3
"""
This Module adds two ints together and returns the sum
Only takes in floats and ints otherwise raise TypeError
When float comes in, int goes out
"""
def add_integer(a, b=98):
    """
    add_integer: adds two ints together and checks if the intake is right
    """
    if isinstance(a,(int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b,(int, float)) is False:
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
