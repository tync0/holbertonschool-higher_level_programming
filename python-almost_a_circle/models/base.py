#!/usr/bin/python3
"""Represents the Base class."""

import json
import os


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

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list.

        Args:
            json_string (str): A JSON string.
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a JSON file.

        Args:
            cls (class): The class of the objects.
            list_objs (list): The list of objects to be saved.
        """
        if list_objs is None:
            list_dictionary = []
        else:
            list_dictionary = [obj.to_dictionary() for obj in list_objs]

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dictionary))

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance of the class based on the given dictionary.

        Args:
            dictionary (dict): A dictionary containing
            the attributes of the instance.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a JSON file and returns a list of instances.

        Returns:
            list: A list of instances loaded from the JSON file.
        """
        filename = "{}.json".format(cls.__name__)
        if not os.path.isfile(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            json_str = f.read()
            list_from_json = cls.from_json_string(json_str)
            new = []
            for i in list_from_json:
                a = cls.create(**i)
                new.append(a)
            return new
