#!/usr/bin/python3
"""class Square that inherits from Rectangle
   (9-rectangle.py)
   (task based on 10-square.py).
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits from Rectangle
        (9-rectangle.py)
        (task based on 10-square.py).
    """

    def __init__(self, size):
        """ Constructing the square
            using self, size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ print(self) method """
        return '[Square] {:d}/{:d}'.format(self.__size, self.__size)
