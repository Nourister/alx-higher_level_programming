#!/usr/bin/python3

"""Define a object-to-text file with json function"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation
    Args:
    my_obj (str): the string to write to a text file
    filename (str): name of the object
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
