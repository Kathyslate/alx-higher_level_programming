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

    def __str__(self):
        """Prints square"""
        return ("[Square] ({}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """Property retriever for size.

        Returns:
            int: size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Property setter for width of square.
        Args:
            value (int): width of square.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

        Args:
             imported from rectangle
        """
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
