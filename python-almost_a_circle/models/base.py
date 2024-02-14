#!/usr/bin/python3
"""Represents the Base class."""

import json


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
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a JSON file.

        Args:
            cls (class): The class of the objects.
            list_objs (list): The list of objects to be saved.
        """
        if list_objs is None:
            objs = []
        else:
            objs = [objs.to_dictionary for obj in objs]
        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(objs))
