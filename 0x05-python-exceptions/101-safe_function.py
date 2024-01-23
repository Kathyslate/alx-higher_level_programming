#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        rest = fct(*args)
        return rest
    except BaseException as val:
        print("Exception: {}".format(val), file=sys.stderr)
        return None
