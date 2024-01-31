#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        new = []
        for i in matrix:
            row = [x ** 2 for x in i]
            new.append(row)
        return new
