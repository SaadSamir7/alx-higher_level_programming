#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, default 98): The second number.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an int or a float.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
