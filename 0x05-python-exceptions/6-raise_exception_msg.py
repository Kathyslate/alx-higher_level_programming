#!/usr/bin/python3
def raise_exception_msg(message=""):
    if not isinstance(message, str):
        raise ValueError("The message must be a string")
    raise NameError(message)
