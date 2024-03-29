#!/usr/bin/python3
"""Defines a function that reads a text file."""


def read_file(filename=""):
    """Prints the content of UTF8 file to stdout."""
    with open(filename, encoding = 'utf-8') as f:
        print(f.read(), end="")
