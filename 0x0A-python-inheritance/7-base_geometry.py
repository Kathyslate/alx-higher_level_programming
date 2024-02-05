#!/usr/bin/python3
"""BaseGeometry
   based on 6-base_geometry.py
"""


class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception
           with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
