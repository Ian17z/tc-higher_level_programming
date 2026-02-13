#!/usr/bin/python3
'''
Este módulo cria um quadrado.
'''


def print_square(size):
    '''
    size calcula o tamanho do quadrado somente se for inteiro e maior que zero.

    Caso não, a mensagem de erro aparece na tela.
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print('#' * size)
