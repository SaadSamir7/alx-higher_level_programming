#!/usr/bin/python3
"""Square module.
This module contains a class that defines a square and init method that
sets its size and checking if the given values are right. There's also an
area method that returns the area of the square.
"""


class Square:
    """Defines a square."""
    def __init(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
