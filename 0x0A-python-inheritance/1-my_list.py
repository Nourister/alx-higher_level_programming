#!/usr/bin/python3
"""Defines an inherited class Mylist."""

class MyList(list):
    """prints the list, but sorted (ascending sort)."""

    def print_sorted(self):
        print(sorted(self))
