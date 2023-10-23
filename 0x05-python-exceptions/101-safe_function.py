#!/usr/bin/python3
def safe_function(fct, *args):

    try:
        res = fct(*args)
        return res
    except Exception as err:
        import sys
        sys.stderr.write("Exception: {}\n".format(str(err)))
        return None
