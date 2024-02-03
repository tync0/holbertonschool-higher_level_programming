#!/usr/bin/python3
"""Define a Square clas"""


class Square:
    """Document for Square class"""

    def __init__(self, size=0, position=(0,0)):
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not (
                isinstance(value, tuple)
                and len(value) == 2
                and all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Document for area"""
        return self.__size ** 2

    def my_print(self):
        """Document for setter my_print"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()

            for i in range(self.size):
                for _ in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
