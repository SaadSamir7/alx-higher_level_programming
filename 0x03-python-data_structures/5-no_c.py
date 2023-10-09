#!/usr/bin/python3
def no_c(my_string):
    for x in my_string:
        if my_string[x] == 'c' or my_string[x] == 'C':
            del my_string[x]
