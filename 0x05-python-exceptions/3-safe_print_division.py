#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        division_result = a / b if b else None
    except TypeError:
        print("Error: Both operands must be integers or floats")
        return None
    finally:
        print("Inside result: {}".format(division_result))
        return division_result
