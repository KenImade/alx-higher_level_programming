#!/usr/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) < 0:
        return None

    for row in matrix:
        print(' '.join(["{:d}".format(elem) for elem in row]))
