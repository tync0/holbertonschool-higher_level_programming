#!/usr/bin/python3
"""Test for base model"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_as_positive(self):
        base_instance = Base(1)
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(5)
        self.assertEqual(base_instance.id, 5)

    def test_id_as_negative(self):
        base_instance = Base(-18)
        self.assertEqual(base_instance.id, -18)
        base_instance = Base(-2)
        self.assertEqual(base_instance.id, -2)

    def test_id_as_none(self):
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_string_id(self):
        base_instance = Base("Flutter")
        self.assertEqual(base_instance.id, "Flutter")
        base_instance = Base("C > Python")
        self.assertEqual(base_instance.id, "C > Python")

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 123}]), '[{"id": 123}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 123}]'), [{"id": 123}])
