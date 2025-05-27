#!/usr/bin/python3
"""
task_00_abc

this file contains 3 class's:
Animal, Dog, Cat
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    this is a class animal with abstractmethod
    sound, with no body
    """
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    this is a class Dog inherit of Animal
    with method sound returning Bark
    """
    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    this is a class Cat inherit of Animal
    with method sound returning Meow
    """
    def sound(self):
        return "Meow"
