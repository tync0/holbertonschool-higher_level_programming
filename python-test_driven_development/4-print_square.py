"""
    This module contains print_square function.
"""


def print_square(size):
    """
        print_square - prints square with #
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
    print()
