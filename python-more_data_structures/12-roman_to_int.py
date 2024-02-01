#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return None
    roman_string = roman_string[::-1]
    a = 0
    numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
            "M": 1000}
    keys = list(numbers.keys())
    index = keys.index(roman_string[0])
    print(index)
    for i in roman_string:
        for j in range(len(keys)):
            if i == keys[j]:
                if index > j:
                    a -= numbers[i]
                else:
                    a += numbers[i]
                index = j
    return a
