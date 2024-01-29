#!/usr/bin/python3
"""
Defining a class Rectangle
"""



class Rectangle:
    """representing a rectangle"""
    def __init__(self, width=0, height=0):
        """initializing the rectangle"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """getting the attribute width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """setting the attribute width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """getting the attribute height of the rectangle"""
        return self._height

    @height.setter
    def height(self, value):
        """setting the attribute width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value
