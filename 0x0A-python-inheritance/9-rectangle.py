#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry
   (7-base_geometry.py).
   (task based on 8-rectangle.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle inherits from BaseGeomtry
        (7-base_geometry.py).
        (task based on 8-rectangle.py)
    """

    def __init__(self, width, height):
        """ Constructing the rectangle
            using self, width, height
        """
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area of the Rectangle object"""
        return self.__width * self.__height

    def __str__(self):
        """ string represention of Rectangle object """
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
