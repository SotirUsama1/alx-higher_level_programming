#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in matrix[i]:
            if j == len(matrix[i]) - 1:
                print("{:d}".format(matrix[i][j]))
            else:
                print("{:d} ".format(matrix[i][j]))
