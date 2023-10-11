#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """ Write a function that deletes keys with a specific value in dictionary.

All keys having the searched value have to be deleted

Arguments:
    a_dictionary
    value of the pair to be removed

Return:
    a_dictionary after the delete
"""
    temp_dict = {key: value for key, value in a_dictionary.items()}
    for key, val in temp_dict.items():
        if val == value:
            del (a_dictionary[key])

    return a_dictionary
