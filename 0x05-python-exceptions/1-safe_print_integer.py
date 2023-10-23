#!/usr/bin/python3
def safe_print_integer(value):
    """ a function that prints an integer with "{:d}".format().

    Returns:
      True if value has been correctly printed
      (it means the value is an integer)
    """
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
        else:
            raise ValueError
        return True
    except ValueError:
        return False
