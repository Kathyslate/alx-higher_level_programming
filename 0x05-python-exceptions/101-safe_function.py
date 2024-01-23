#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        rest = fct(*args)
    except BaseException as e:
        rest = None
        print("Exception: {}".format(e), file=sys.stderr)
    finally:
        return rest
