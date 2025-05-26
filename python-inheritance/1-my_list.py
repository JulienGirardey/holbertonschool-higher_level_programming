#!/usr/bin/python3
"""
1-my_list

creat class that inherit from list
"""


class MyList(list):
    """
    class MyList
    """
    def print_sorted(self):
        print(sorted(self))
