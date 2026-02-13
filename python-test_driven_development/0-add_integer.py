#!/usr/bin/python3
"""
Module that contains function add_integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    a and b must be integers or floats.
    If a or b is a float, it is converted to an integer.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        The integer addition of a and b.

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(4.2, 5.9)
        9
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
