#!/usr/bin/python3
""" Module that contains class Square,
inheritance of class Rectangle
"""


from inspect import classify_class_attrs
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines properties of Square.

     Attributes:
        imported from rectangle.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Creates new instances of Square

        Args:
            size (int): width and height of square.
        """
        super().__init__(size, size, x, y, id)
