#!/usr/bin/python3

"""
    This module contain a function: matrix_divided
"""


def matrix_divided(matrix, div):
    """
        matrix_divided - This function divides all
        elements of a matrix.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(type(row) is list for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(type(i) in [int, float] for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    new = []
    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(round(i / div, 2))
        new.append(new_row)
    return new
