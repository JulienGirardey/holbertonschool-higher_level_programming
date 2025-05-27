#!/usr/bin/python3
"""
task_05_dragon

this file contains 3 class's:
SwimMixin, FlyMixin and Dragon
"""


class SwimMixin:
    """
    this class contains 1 methods:
    swim to print: The creature swims!
    """
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """
    this class contains 1 methods:
    fly to print: The creature flies!
    """
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    this class contains 1 methods:
    roar to print: The dragon roars!
    """
    def roar(self):
        print("The dragon roars!")
