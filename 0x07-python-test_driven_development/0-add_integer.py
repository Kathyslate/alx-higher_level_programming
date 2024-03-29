#!/usr/bin/python3
"""function that adds 2 integers"""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: first int.
        b: must be 98.

    Raises:
        TypeError: if a, b are not integers or float.

    Returns:
        the addition of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
