#!/usr/bin/python3

def safe_print_integer(value):
    is_value = False
    try:
        print("{:d}".format(value))
    except TypeError:
        return is_value
    else:
        is_value = True
    return is_value
