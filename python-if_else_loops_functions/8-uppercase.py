#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) <= 122 and ord(i) >= 97:
            i = chr(ord(i) - 32)
        print("{}".format(i), end = "")
    print()
