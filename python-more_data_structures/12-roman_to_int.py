#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    roman_string = roman_string[::-1]
    a = 0
    keys = ["I", "V", "X", "L", "C", "D", "M"]
    numbers = [1, 5, 10, 50, 100, 500, 1000]
    index = keys.index(roman_string[0])
    for i in roman_string:
        for j in range(len(keys)):
            if i == keys[j]:
                if index > j:
                    a -= numbers[j]
                else:
                    a += numbers[j]
                index = j
    return a
