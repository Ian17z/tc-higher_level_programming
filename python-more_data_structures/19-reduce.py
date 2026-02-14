#!/usr/bin/python3
from functools import reduce

def calc_average(a_dictionary):
    """
    Calcula a média dos salários e idades de uma lista de dicionários
    """
    total_salary = reduce(lambda acc, person: acc + person['salary'], a_dictionary, 0)
    total_age = reduce(lambda acc, person: acc + person['age'], a_dictionary, 0)
    
    n = len(a_dictionary)
    return (total_salary / n, total_age / n)