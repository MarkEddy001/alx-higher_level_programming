#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """ Write a function that prints a dictionary by ordered keys.

        Arguments:
                a_dictionary

        Return:
                nothing
   """
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))
