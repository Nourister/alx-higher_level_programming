#!/usr/bin/python3

"""Defines if object exactly an instance of the specified class."""

def is_same_class(obj, a_class):
    """Checking if the object is exactly an instance of the specified class

    Args:
        obj (a ny): checks any object
        a_class (type): class to match the object to

    Returns:
        True if the object is exactly an instance of the specified class
        otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
