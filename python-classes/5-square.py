#!/usr/bin/python3
"""Define a Square clas"""


class Square:
    """Document for Square class"""

    def __init__(self, size=0):
        """Document for init"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Document for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Document for setter size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Document for area"""
        return self.__size ** 2

    def my_print(self):
        """Document for setter my_print"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
