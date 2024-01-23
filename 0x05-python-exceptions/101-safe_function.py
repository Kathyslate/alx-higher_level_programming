#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        rest = fct(*args)
    except BaseException as eval:
        rest = None
        print("Exception: {}".format(eval), file=sys.stderr)
    finally:
        return rest
