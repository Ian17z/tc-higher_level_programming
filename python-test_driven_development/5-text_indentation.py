#!/usr/bin/python3
"""
Módulo que contém a função text_indentation.
"""


def text_indentation(text):
    """
    Imprime um texto com duas novas linhas após '.', '?' e ':'.

    >>> text_indentation("Hello. How are you? I am fine:")
    Hello.

    How are you?

    I am fine:

    >>> text_indentation("  Hello.   World?  Yes:  ")
    Hello.

    World?

    Yes:

    >>> text_indentation(None)
    Traceback (most recent call last):
    ...
    TypeError: text must be a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = True

    for char in text:
        if start and char == " ":
            continue

        print(char, end="")

        if char in ".?:":
            print("\n")
            start = True
        else:
            start = False
