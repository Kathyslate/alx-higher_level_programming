#!/usr/bin/python3
"""Defines a class LockedClass"""

class LockedClass:
    """
    A class LockedClass with no class or object attribute,
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.

    Attributes:
        first_name (str): a person's first name.
    """

    __slots__ = ["first_name"]
    def __init__(self):
    """initiates instances for locked class"""
         self.first_name = "first_name"
