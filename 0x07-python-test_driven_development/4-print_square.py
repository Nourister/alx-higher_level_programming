#!/usr/bin/python3

""" Define printing of squares """
def print_square(size):
    """ print a size of a square with # character

    Args:
    size(int): height/width of the square
    Raises:
    TypeError: size is not an integer
    ValueError: size must be < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="")for i in range(size)]
        print("")
