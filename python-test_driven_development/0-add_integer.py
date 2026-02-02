#!/usr/bin/python3
'''
Este módulo devolve uma função que é capaz de fazer a soma inteira de dois números inteiros ou flutuantes.
'''
def add_integer(a, b=98):
    '''
    Try: Soma dois números inteiros ou flutuantes.
    
    Execept: Caso a ou b não se enquadrem na função
    '''
    try:
        a = int(a)
    except (TypeError, ValueError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (TypeError, ValueError):
        raise TypeError("b must be an integer")

    return a + b
