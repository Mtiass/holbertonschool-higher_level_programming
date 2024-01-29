#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = [row[:] for row in matrix]  # Makes a deep copy
    for fila in newmatrix:
        for i in range(len(fila)):
            fila[i] = fila[i] * fila[i]
    return newmatrix
