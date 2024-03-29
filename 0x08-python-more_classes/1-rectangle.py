#!/usr/bin/python3
"""
Defining a class Rectangle
"""


class Rectangle:
    """representing a rectangle"""
    def __init__(self, width=0, height=0):
        """initializing the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getting the attribute width of the rectangle"""
        return self._Rectangle_width

    @width.setter
    def width(self, value):
        """setting the attribute width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle_width = value

    @property
    def height(self):
        """getting the attribute height of the rectangle"""
        return self._Rectangle_height

    @height.setter
    def height(self, value):
        """setting the attribute width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._Rectangle_height = value
