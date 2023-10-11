#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dict = sorted(a_dictionary.keys())
    for x in sort_dict:
        print("{:s} : {:s}".format(x, a_dictionary[x]))
