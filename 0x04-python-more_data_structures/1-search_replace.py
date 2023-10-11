#!/usr/bin/python3
def search_replace(my_list, search, replace):

    """ a function that replaces all occurrences of an element
        by another in a new list

     Arguments:     (my_list) is the initial list
                    (search) is the element to replace in the list
                    (replace) is the new elemen

    Return:         a new list with all the elements exept for
                     search replace by replace
    """

    new_list = [replace if i == search else i for i in my_list]
    return (new_list)
