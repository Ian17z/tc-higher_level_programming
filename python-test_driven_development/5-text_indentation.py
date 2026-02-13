#!/usr/bin/python3
"""
Printa um texto com 2 novas linhas a cada ., ? ou : na frase digitada.
"""


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("Deverá ser uma string")

    espaco = False

    for char in text:
        if espaco and char == " ":
            continue

        espaco = False
        print(char, end="")

        if char in ".?:":
            print("\n")
            espaco = True