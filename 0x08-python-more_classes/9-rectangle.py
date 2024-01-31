#!/usr/bin/python3
"""
Defining a class Rectangle
"""


class Rectangle:
    """representing a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializing the rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        return "\n".join(str(self.print_symbol) * self._Rectangle_width for j in range(self._Rectangle_height))

    def __repr__(self):
        """return a string representation of the rectangle to be able to recreate a new instance"""
        return "Rectangle({}, {})".format(self._Rectangle_width, self._Rectangle_height)

    def __del__(self):
        """Print the message Bye rectangle"""
        print("Bye rectangle...")
        if self._Rectangle_width == 0 or self._Rectangle_height == 0:
            return
        if self._Rectangle_width is None or self._Rectangle_height is None:
            return
        del self._Rectangle_width
        del self._Rectangle_height
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
