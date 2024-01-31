#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = set(my_list)
    cem = 0
    for i in new:
        cem += i
    return cem
