#!/usr/bin/python3


"""Documented Module"""


import sys
import os

to_json = __import__("5-save_to_json_file").save_to_json_file
from_json = __import__("6-load_from_json_file").load_from_json_file
filename = "add_item.json"
if os.path.isfile(filename):
    new_list = from_json(filename)
else:
    new_list = []
new_list.extend(sys.argv[1:])
to_json(new_list, filename)
