#!/usr/bin/python3
"""class Square that inherits from Rectangle
   (9-rectangle.py)
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits attributes from Rectangle class """

    def __init__(self, size):
        """ Constructing the square
            using self, size
        """
        if self.integer_validator('size', size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns area of Square object"""
        return super().area()
