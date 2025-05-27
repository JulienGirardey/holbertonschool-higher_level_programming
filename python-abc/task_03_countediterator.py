#!/usr/bin/python3
"""
task_03_countediterator

this file contains the class:
CountedIterator
"""


class CountedIterator:
    """
    this class contains 3 methods
    init, get_count and next
    """
    def __init__(self, some_iterable):
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration("No more items to iterated.")
