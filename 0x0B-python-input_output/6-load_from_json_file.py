#!/usr/bin/python3
""" function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.
       You don’t need to manage exceptions
       if the JSON string doesn’t represent an object.

    Args:
        filename (str): name of the file.

    Returns:
        object: object.
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
