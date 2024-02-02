#!/usr/bin/python3
def roman_to_int(roman_string):

    if len(roman_string) == 0 or roman_string is None:
        return (0)

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(roman_string)):

        current = roman[roman_string[i]]

        if i == 0:
            result += current
        else:
            prev = roman[roman_string[i - 1]]
            if current > prev:
                diff = current - prev
                arrange = diff - prev
                result += arrange
            else:
                result += current

    return result
