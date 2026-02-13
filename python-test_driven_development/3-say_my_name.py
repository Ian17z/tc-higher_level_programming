#!/usr/bin/python3
"""
Este módulo devolve o primeiro e último nome de uma pessoa.
"""


def say_my_name(first_name, last_name=""):
    """
    Printa uma função com o primeiro e último nome de uma pessoa.

    Caso encontre algum erro a mensagem indica que deve ser uma string tanto no primeiro quanto no último.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
