#!/usr/bin/python3
"""
6-load_from_json_file module
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file - loads an object from JSON file.
    Args:
        filename: name of the file
    """
    with open(filename, "r") as f:
        json_file = json.load(f)
        return json_file
