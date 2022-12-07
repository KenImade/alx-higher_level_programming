#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    
    matrix_copy = matrix.copy()
    
    squared_matrix = [[x * x for x in row] for row in matrix_copy]

    return squared_matrix

