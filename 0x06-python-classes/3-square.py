#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square and init method that
sets its size and checking if the given values are right. There's also an
area method that returns the area of the square.
"""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
