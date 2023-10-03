#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the value of the division, otherwise: None"""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
        return (div)
