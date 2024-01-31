#!/usr/bin/python3
"""This module adds all arguments to a Python list and
saves them to a file"""
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


arguments = sys.argv[1:]
args_list = []
file = "add_item.json"

try:
    existing_data = load_from_json_file(file)

    if existing_data is not None and isinstance(existing_data, list):
        args_list = existing_data
except FileNotFoundError:
    pass

args_list.extend(arguments)
save_to_json_file(args_list, file)
