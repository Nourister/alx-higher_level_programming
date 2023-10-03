#!/usr/bin/python3

"""adds all arguments to a Python list, and then save them to a file"""

import sys


def save_to_json_file(my_obj, filename):
    import json

    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)

def load_from_json_file(filename):


    import json

    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


# File name where data will be stored
filename = "add_item.json"

# Try to load existing items if the file exists,
# otherwise start with an empty list
try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

# Append command line arguments to the list
items.extend(sys.argv[1:])

# Save updated items back to the file
save_to_json_file(items, filename)

