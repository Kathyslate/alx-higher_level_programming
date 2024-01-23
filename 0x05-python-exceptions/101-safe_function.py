#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except BaseException as val:
        print("Exception: {}".format(val), file=sys.stderr)
        return None
