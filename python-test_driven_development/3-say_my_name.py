#!/usr/bin/python3

"""
    This module contains say_my_name function.
"""

def say_my_name(first_name, last_name=""):
    """
        say_my_name - Prints My name is <first name> <last name>
    """

    if not type(first_name) is str:
        raise TypeError("irst_name must be a string")
    if not type(last_name) is str:
        raise TypeError("ast_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
