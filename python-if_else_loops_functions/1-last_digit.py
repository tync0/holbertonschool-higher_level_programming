#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
    digit = -digit
print(f"Last digit of {number} is {digit} and is ", end = "")
if digit == 0:
    print("0")
elif digit > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
