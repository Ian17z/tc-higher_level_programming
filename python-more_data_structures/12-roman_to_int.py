#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(string_romana, str):
        return 0
    mapa_romano = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    valor_anterior = 0
    for caractere in reversed(string_romana.upper()):
        valor_atual = mapa_romano.get(caractere, 0)
        if valor_atual < valor_anterior:
            total -= valor_atual
        else:
            total += valor_atual    
        valor_anterior = valor_atual
    return total
