#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary)
    keys.sort()
    new_dict = {i: a_dictionary[i] for i in keys}
    for key, value in new_dict.items():
        print("{}: {}".format(key, value))
