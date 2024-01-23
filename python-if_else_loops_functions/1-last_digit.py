#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    ltd = number % 10
elif number < 0:
    ltd = -(abs(number) % 10)
else:
    ltd = 0
if ltd != 0:
    if ltd > 5:
        print(f"Last digit of {number} is {ltd} and is greater than 5")
    elif ltd < 6:
        print(f"Last digit of {number} is {ltd} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {ltd} and is 0")
