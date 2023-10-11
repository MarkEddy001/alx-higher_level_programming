#!/usr/bin/python3
def best_score(a_dictionary):
    """ Write a function that returns a key with the biggest integer value.

    Arguments:
            a_dictionary

    Return:
            a key with the biggest integer value
    """

    if not a_dictionary:
        return None

    key_max_value = ""
    max_value = 0
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            key_max_value = key

    return key_max_value
