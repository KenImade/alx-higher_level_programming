#!/usr/bin/python3
"""A class MyList that inherits from list
"""


class MyList(list):
    """A custom list
    """
    def print_sorted(self):
        """
        prints the list in sorted order
        """
        print(sorted(self))
