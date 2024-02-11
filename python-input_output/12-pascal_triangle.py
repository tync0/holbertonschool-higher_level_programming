#!/usr/bin/python3


"""Documented Module"""


def pascal_triangle(n):
    """Function Document"""
    if n <= 0:
        return []
    new = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i >= 2 and not j == 0 and not j == i:
                a = new[i - 1][j] + new[i - 1][j - 1]
                row.append(a)
            else:
                row.append(1)
        new.append(row)
    return new
