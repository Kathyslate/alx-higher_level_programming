#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ class Square that defines a square"""
    def __init__(self, size=0):
        """ init square

        Args:
            value (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """int: private size.

        Returns:
            Private size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets value into size, must be int.

        Args:
            value (int): size of the square.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of the square

    def area(self):
        """returns the area

        Returns:
            area.
        """
        return self.__size * self.__size

    def __lessthan__(self, other):
        return self.size < other.size

    def __lessequal__(self, other):
        return self.size <= other.size

    def __equal__(self, other):
        return self.size == other.size

    def __notequal__(self, other):
        return self.size != other.size

    def __greatequal__(self, other):
        return self.size >= other.size
    def __greatthan__(self, other):
        return self.size > other.size
