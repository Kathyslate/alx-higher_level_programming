#!/usr/bin/python3
"""class MyList that inherits from list
"""


class MyList(list):
    """ This class inherits from list() """

    def print_sorted(self):
        """ that prints the list
        but sorted (ascending sort) """
        print(sorted(self))
