#!/usr/bin/python3
"""
Modulo divide todos os elementos da matriz.
"""

def matrix_divided(matrix, div):
    """
    Divide todos os elementos.

    Args:
        matrix (list): lista que contem os valores
        div (int/float): divisor

    Returns:
        Nova matriz com os elementos divididos

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
    [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

    >>> matrix_divided([[1.5, 3], [6, 9]], 3)
    [[0.5, 1.0], [2.0, 3.0]]

    >>> matrix_divided([[1, 2], [3, 4]], 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero

    >>> matrix_divided([[1, 2], [3, "4"]], 2)
    Traceback (most recent call last):
    ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats

    >>> matrix_divided([[1, 2], [3]], 2)
    Traceback (most recent call last):
    ...
    TypeError: Each row of the matrix must have the same size

    >>> matrix_divided([[1, 2], [3, 4]], "2")
    Traceback (most recent call last):
    ...
    TypeError: div must be a number
    """

    if (not isinstance(div, (int, float))):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(num, (int, float))
                    for row in matrix for num in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError(
            "Each row of the matrix must have the same size"
        )

    return [[round(num / div, 2) for num in row] for row in matrix]
