#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """ a function that prints an integer with "{:d}".format().

    Returns:
      True if value has been correctly printed
      (it means the value is an integer)
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        sys.stderr.write("Exception: {}\n".format(str(err)))
        return False
