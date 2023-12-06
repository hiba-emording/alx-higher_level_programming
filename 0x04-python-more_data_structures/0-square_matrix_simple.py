#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for row in matrix:
        sq_row = list(map(lambda x: x ** 2, row))
        sq_matrix.append(sq_row)
    return sq_matrix
