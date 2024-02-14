#!/usr/bin/python3
"""Represents the Base class."""


class Base:
    """Represents the Base class.

    Base class for all other classes in the model package.

    Attributes:
        __nb_objects (int): The number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of the Base class.

        Args:
            id (int): The identity of the new Base.
        """
        if id == None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
