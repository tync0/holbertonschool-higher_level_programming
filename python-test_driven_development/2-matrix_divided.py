#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of "
        "integers/floats")
    if not all(type(row) is list for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
        "integers/floats")
    if all(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if (type(i) not in [int, float] for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
        "integers/floats")
    new = []
    for row in matrix:
        for i in row:
            new.append(round(i / div, 2))
    return new
