#!/usr/bin/python3
"""
Printa um texto com 2 novas linhas a cada ., ? ou : na frase digitada.
"""


def text_indentation(text):
    '''
    A cada ., ? ou : é gerada 2 novas linhas.

    Se não, é necessário digitar uma string ou algo
    '''
    if type(text) is not str:
        raise TypeError("DEVE SER STRING")

    for char in text:
        if char in ".?:":
            print(char)
            print()
        else:
            print(char, end="")
