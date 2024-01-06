#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = None
    for i in my_list:
        if max_val is None or i > max_val:
            max_val = i
    return max_val
