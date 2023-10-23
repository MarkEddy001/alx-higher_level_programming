#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ a function that prints the first elements of a list only integers. """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count = count + 1
        except TypeError:
            pass
        except ValueError:
            pass
        except IndexError:
            raise
    print()
    return count
