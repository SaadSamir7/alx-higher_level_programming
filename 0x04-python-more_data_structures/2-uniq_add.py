#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = set(my_list)
    res = 0
    for x in add:
        res += x

    return res
