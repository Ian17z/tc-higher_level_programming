#!/usr/bin/python3
from functools import reduce

def calc_average(a_dictionary):
    """
    Recebe uma lista de dicionários com as chaves 'age' e 'salary'
    e imprime a média dos valores dessas chaves.
    """
    if not a_dictionary:
        print("Lista vazia.")
        return
    
    # Soma de ages
    total_age = reduce(lambda acc, d: acc + d['age'], a_dictionary, 0)
    # Soma de salaries
    total_salary = reduce(lambda acc, d: acc + d['salary'], a_dictionary, 0)
    
    average_age = total_age / len(a_dictionary)
    average_salary = total_salary / len(a_dictionary)
    
    print(f'The average salary is R${average_salary:0.2f} with an average age of {average_age}')

data = [
    {'name': 'Alice', 'age': 50, 'salary': 5000},
    {'name': 'Bob', 'age': 30, 'salary': 7000},
    {'name': 'Charlie', 'age': 35, 'salary': 9000},
    {'name': 'Dave', 'age': 40, 'salary': 11000},
    ]
calc_average(data)