#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ print the content of linst

    catch index of range error
    """
    count = 0
    if not list:
        return count
    for i in range(x):
        try:
            print(my_list[i], end="")
            count = count + 1
        except IndexError:
            print()
            return count
    print()
    return count
