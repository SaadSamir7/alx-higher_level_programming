#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if row:
            print(" ".join(["{:d}".format(num) for num in row]))
        else:
            print()
