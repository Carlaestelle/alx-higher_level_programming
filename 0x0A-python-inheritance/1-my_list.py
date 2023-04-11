#!/usr/bin/python3
"""Contains the class MyList."""


class MyList(list):
    """A subclass of list."""
    def __init__ (self):
        """initializing object."""
        super().__init__()

    def print_sorted(self):
        """Prints sorted list."""
        print(sorted(self))
