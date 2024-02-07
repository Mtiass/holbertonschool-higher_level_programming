#!/usr/bin/python3
"""
This module defines a script that adds all arguments to
a Python list, and then save them to a file.
"""
from sys import argv
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filena = "add_item.json"
try:
    jlist = load_from_json_file(filena)
except FileNotFoundError:
    jlist = []

for con in range(1, len(argv)):
    jlist.append(argv[con])

save_to_json_file(jlist, filena)
