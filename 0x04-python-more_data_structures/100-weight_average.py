#!/usr/bin/python3
def weight_average(my_list=[]):

    if not my_list:
        return 0
    _sum = 0
    _numbers = 0
    for tp in my_list:
        _sum += tp[0] * tp[1]
        _numbers += tp[1]

    return _sum / _numbers
