#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """ a function that divides element by element 2 lists.
    Returns:
            a new list (length = list_length) with all divisions
    """
    new_list = []
    result = 0
    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and \
                    isinstance(my_list_2[i], (int, float)):
                result = my_list_1[i] / my_list_2[i]
            else:
                raise TypeError
        except TypeError:
            print("wrong type")
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            new_list.append(result)

    return new_list
