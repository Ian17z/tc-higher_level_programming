#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    novamatrix = []

    for i in matrix:
        novoi = []
        for j in i:
            novoi.append(j * j)
        novamatrix.append(novoi)
    return novamatrix
