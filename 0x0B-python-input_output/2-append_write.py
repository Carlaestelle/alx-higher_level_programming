#!/usr/bin/python3
"""Defines a function that appends string"""


def append_write(filename="", text=""):
    """Appends a string to a UTF-8 text file.

    Args:
        filename: The name of file to be appended.
        text: Text to be added to file.
    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding = "utf-8") as f:
        return f.write(text)
