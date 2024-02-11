#!/usr/bin/python3


"""Documented Module"""


class Student:
    """Documented Module"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for i in attrs:
            if i in self.__dict__.keys():
                new_dict[i] = self.__dict__[i]
        return new_dict

    def reload_from_json(self, json):
        for i in json:
            setattr(self, i, json[i])
