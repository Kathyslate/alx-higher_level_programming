#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        rest = fct(*args)
    except BaseException as val:
        rest =  None
        print("Exception: {}".format(val), file=sys.stderr)
    return rest
