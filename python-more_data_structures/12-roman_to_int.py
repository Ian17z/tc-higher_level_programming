#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    valor_romano = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    valor_anterior = 0

    for char in reversed(roman_string):
        valor = valor_romano.get(char, 0)

        if valor < valor_anterior:
            total -= valor
        else:
            total += valor

        valor_anterior = valor

    return total
