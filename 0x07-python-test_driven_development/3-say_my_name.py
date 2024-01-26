#!/usr/bin/python3
"""
Module function say_my_name
Prints a given first name and last name.
"""


def say_my_name(first_name, last_name=""):
    """Prints a string with <first_name>
    and <last_name>.
    """

    # Check if first_name is a
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # Print the message
    print("My name is {} {}".format(first_name, last_name))
