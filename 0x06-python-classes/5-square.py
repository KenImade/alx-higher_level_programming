#!/usr/bin/python3
"""
This module defines a Square class

It implements value and type check for its attributes
"""


class Square:
    """Square implementation
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints a square with the corresponding size
        """
        if (self.__size == 0):
            print("")

        i = 0
        while (i < self.__size):
            print("#" * self.__size)
            i += 1
