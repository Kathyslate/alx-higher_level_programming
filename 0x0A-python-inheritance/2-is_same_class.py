#!/usr/bin/python3
""" returns True if the object is exactly an instance of the specified class
    otherwise False
"""


def is_same_class(obj, a_class):
    """ Checks if obj is exactly an instance of a_class
        returns the object if it is
    """
    return type(obj) == a_class
