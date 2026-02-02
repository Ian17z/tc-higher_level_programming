#!/usr/bin/python3
'''
Este módulo é capaz de dividir cada número dentro da matriz
'''
def matrix_divided(matrix, div):
    '''
    Divisão de matrizes.
    '''
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number") 
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not matrix or not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    tamanho_linha = len(matrix[0])
    nova_matriz = []
    for linha in matrix:
        if len(linha) != tamanho_linha:
            raise TypeError("Each row of the matrix must have the same size")
        
        nova_linha = []
        for elemento in linha:
            if not isinstance(elemento, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            resultado = round(elemento / div, 2)
            nova_linha.append(resultado)
        nova_matriz.append(nova_linha)
    return nova_matriz