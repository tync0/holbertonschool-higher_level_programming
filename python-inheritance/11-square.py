#!/usr/bin/python3


"""Module doc"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Rectangle class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size**2

    def __str__(self):
        print("[Square] {}/{}".format(self.__size, self.__size))
