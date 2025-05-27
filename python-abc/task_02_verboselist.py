#!/usr/bin/python3
"""
task_02_verboselist

this file contains the class:
VerboseList inherit of list
"""


class VerboseList(list):
    """
    this class contains 4 methods:
    append, extend, remove and pop
    """
    def append(self, object):
        super().append(object)
        print("Added [{}] to the list.".format(object))

    def extend(self, iterable):
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(len(iterable)))

    def remove(self, value):
        print("Removed [{}] from the list.".format(value))
        return super().remove(value)

    def pop(self, index=-1):
        value = self[index]
        print("Popped [{}] from the list.".format(value))
        return super().pop(index)
