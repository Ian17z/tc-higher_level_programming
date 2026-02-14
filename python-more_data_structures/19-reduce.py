#!/usr/bin/python3
#!/usr/bin/env python3
from functools import reduce

def calc_average(a_dictionary):
    """
    Calcula a média dos salários e idades de uma lista de dicionários
    """
    # Verificação simples: se não for lista, retorna (0,0)
    if not isinstance(a_dictionary, list):
        return (0, 0)
    
    # Se a lista estiver vazia
    if len(a_dictionary) == 0:
        return (0, 0)
    
    # Usando reduce para somar salários
    total_salary = 0
    total_age = 0
    
    for person in a_dictionary:
        if isinstance(person, dict):
            total_salary += person.get('salary', 0)
            total_age += person.get('age', 0)
    
    n = len(a_dictionary)
    return (total_salary / n, total_age / n)