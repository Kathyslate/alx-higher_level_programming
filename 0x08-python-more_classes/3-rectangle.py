#!/usr/bin/python3
"""
Defining a class Rectangle
"""


class Rectangle:
    """representing a rectangle"""
    def __init__(self, width=0, height=0):
        """initializing the rectangle"""
        self._Rectangle_height = height
        self._Rectangle_width = width

    def area(self):
        """returns the area of the rectangle"""
        return self._Rectangle_width * self._Rectangle_height

    def perimeter(self):
        """returns the calculated area of the rectangle"""
        if self._Rectangle_width == 0 or self._Rectangle_height == 0:
            return 0
        return 2 * (self._Rectangle_width + self._Rectangle_height)

    @property
    def width(self):
        """getting the attribute width of the rectangle"""
        return self._Rectangle_width

    @width.setter
    def width(self, value):
        """setting the attribute width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle_height = value

    def __str__(self):
        """print the rectangle with the character #"""
        if self._Rectangle_width == 0 or self._Rectangle_height == 0:
            return ""
        return "\n".join(["#" * self._Rectangle_width] * self._Rectangle_height)
