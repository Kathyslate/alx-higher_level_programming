#!/usr/bin/python3
def safe_print_integer_err(value):
    try:
        print("{:d}".(value))
        return True
    except Exception:
        print("Exception: {} is not an integer".format(value), file=sys.stderr)
        return False
