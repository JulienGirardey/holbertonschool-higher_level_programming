#!/usr/bin/python3
"""
task_04_flyingfish

this file contains 3 class:
Fish, Bird and FlyingFish
"""


class Fish:
    """
    this class contains 2 methods:
    swim and habitat
    """
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


class Bird:
    """
    this class contains 2 methods:
    fly and habitat
    """
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    this class contains 4 methods:
    fly, swim, habitat and mro
    """
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")

    def __mro__(self):
        print(FlyingFish.mro())
