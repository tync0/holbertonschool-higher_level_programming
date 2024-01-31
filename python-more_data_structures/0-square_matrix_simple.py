#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
        new = []
        for i in range(len(matrix)):
            row = [x ** 2 for x in row]
            new.append(row)
        return new
