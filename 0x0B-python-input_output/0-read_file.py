#!/usr/bin/python3

def read_file(filename=""):
    """Read and print the content of a text file to stdout.

    Args:
        filename (str): the text file to read (default empty string).

    Note:
        This func doesnt handle file permission or exceptions.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
