#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in matrix:
            for j in range(len(i)):
                if j == len(i) - 1:
                    print("{}".format(i[j]), end="")
                else:
                    print("{}".format(i[j]), end=" ")
            print()
