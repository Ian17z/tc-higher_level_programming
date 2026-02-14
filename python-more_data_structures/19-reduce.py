#!/usr/bin/python3
from functools import reduce

def calc_average(a_dictionary):
    """
    Calcula a média dos salários e idades de uma lista de dicionários
    """
    try:
        # Soma todos os salários usando reduce
        total_salary = reduce(lambda acc, person: acc + person['salary'], a_dictionary, 0)
        
        # Soma todas as idades usando reduce
        total_age = reduce(lambda acc, person: acc + person['age'], a_dictionary, 0)
        
        # Calcula as médias
        n = len(a_dictionary)
        return (total_salary / n, total_age / n)
    except:
        # Se algo der errado, retorna (0, 0)
        return (0, 0)