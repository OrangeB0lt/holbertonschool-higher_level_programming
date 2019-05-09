#!/usr/bin/python3
def roman_to_int(roman_string):
    romeNum = {
        'I': 1, 'V': 5,
        'X': 10, 'L': 50,
        'C': 100, 'D': 500,
        'M': 1000
    }
    arabNum = 0

    if roman_string is None or not isinstance(roman_string, str):
        return arabNum

    length = len (roman_string)
    index = 0

    while index < length:
        number1 = romeNum[roman_string[index]]

        if index + 1 < length:
            number2 = romeNum[roman_string[index + 1]]

            if number2 <= number1:
                arabNum += number1
                index += 1
            else:
                arabNum += number2 - number1
                index += 2
        else:
            arabNum += number1
            index += 1
    return arabNum
