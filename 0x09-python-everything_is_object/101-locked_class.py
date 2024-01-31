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
    def __setattr__(self, key, value):
    """initiates instances for locked class"""
        if key != "first_name" and not hasattr(self, key):
            raise AttributeError("Cannot create new instance attribute")
        super().__setattr__(key, value)
