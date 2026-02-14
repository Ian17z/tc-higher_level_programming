#!/usr/bin/env python3
from functools import reduce

def calc_average(a_list_of_dictionaries):
    if not a_list_of_dictionaries:
        return 0, 0

    # Usamos o reduce para somar 'age' e 'salary'
    # O terceiro argumento {} é o valor inicial do acumulador (acc)
    totals = reduce(
        lambda acc, curr: {
            'age': acc['age'] + curr.get('age', 0),
            'salary': acc['salary'] + curr.get('salary', 0)
        },
        a_list_of_dictionaries,
        {'age': 0, 'salary': 0}
    )

    n = len(a_list_of_dictionaries)
    avg_age = totals['age'] / n
    avg_salary = totals['salary'] / n

    # O output desejado pelo seu sistema de correção:
    print(f"The average salary is R${avg_salary:.2f} with an average age of {avg_age}")
    
    return avg_salary, avg_age