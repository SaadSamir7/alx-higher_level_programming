#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cntr = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            cntr = cntr + 1
        except IndexError:
            continue
    print("")
    return cntr
