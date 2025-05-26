#!/usr/bin/python3
"""
1-my_list

creat class that inherit from list
"""


class MyList(list):
    """
    class MyList with a function
    to sort a list
    """

    def print_sorted(self):
        """
        that sort the actual list and
        print it
        """
        print(sorted(self))
