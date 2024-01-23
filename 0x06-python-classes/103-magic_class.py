#!/usr/bin/python3
"""Defines a class MagicClass"""
import math


class MagicClass:
    """
    Class that defines properties of MagicClass.

    Attributes:
        radius: radius.
    """
    def __init__(self, radius=0):
        """Creates new instances of MagicClass.

        Args:
            radius: radius.

        Raises:
            TypeError: radius must be a number .
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self._MagicClass__radius = radius

    def area(self):
        """Returns area

        Returns: area.
        """
        return math.pi * self._MagicClass__radius ** 2

    def circumference(self):
        """Returns circumference

        Returns: circumference.
        """
        return 2 * math.pi * self._MagicClass__radius
