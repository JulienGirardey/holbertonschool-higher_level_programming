#!/usr/bin/python3
"""
1-my_list

in this module we have the class MyList
contains print_sorted method
"""


class MyList(list):
    """
    this is a class for a create square
    and have print_sorted method to print it
    """

    def print_sorted(self):
        """
        that sort the actual list and
        print the list given
        """
        print(sorted(self))
