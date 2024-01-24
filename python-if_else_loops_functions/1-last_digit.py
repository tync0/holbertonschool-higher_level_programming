#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    digit = - (-1 * number % 10)
else:
    digit = number % 10
print(f"Last digit of {number} is {digit} and is", end = " ")
if digit < 6 and digit != 0:
    print("less than 6 and not 0")
elif digit > 5:
    print("greater than 5")
else:
    print("0")
