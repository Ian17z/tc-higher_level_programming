#!/usr/bin/python3
'''
Este módulo devolve uma função que é capaz de fazer a soma inteira de dois números inteiros ou flutuantes.
'''
def add_integer(a, b=98):
    '''
    Try: Soma dois números inteiros ou flutuantes.
    
    Execept: Caso a ou b não se enquadrem na função.
    '''
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
