#!/usr/bin/python3

"""Define a file-appending function."""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)

    Args:
        filename (str): Name to append to
        text (str): string to append on the file
    Return:  returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
