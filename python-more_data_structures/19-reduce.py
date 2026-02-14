#!/usr/bin/python3
from functools import reduce
def calc_average(a_dictionary):
    if not a_dictionary:
        return 0, 0
    somas = reduce(
        lambda acc, curr: {
            'age': acc['age'] + curr.get('age', 0),
            'salary': acc['salary'] + curr.get('salary', 0)
        },
        a_dictionary,
        {'age': 0, 'salary': 0}
    )

    total_itens = len(a_dictionary)
    
    avg_age = somas['age'] / total_itens
    avg_salary = somas['salary'] / total_itens

    return avg_salary, avg_age