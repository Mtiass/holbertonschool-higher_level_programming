#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for fila in matrix:
        for i in range(0, len(fila)):
            print("{:d}".format(fila[i]), end=' ' if i < len(fila) - 1 else '')
        print()
