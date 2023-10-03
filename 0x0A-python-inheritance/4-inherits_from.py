#!/usr/bin/python3

"""Defines an inherited class-checking function."""

def inherits_from(obj, a_class):
    """checks if an object is an instance of a class that inherited

    Args:
        obj (any): An object to check
        a_class (type): A class to check object to

    Returns:
         if the object is an instance of a class that inherited
         from the specified class ; otherwise False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
