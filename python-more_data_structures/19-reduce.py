#!/usr/bin/python3
from functools import reduce

def calc_average(a_dictionary):
    if not a_dictionary:
        return 0, 0

    # O segredo é o terceiro argumento: {'age': 0, 'salary': 0}
    # Isso garante que 'acc' seja SEMPRE um dicionário desde o início
    somas = reduce(
        lambda acc, curr: {
            'age': acc['age'] + curr.get('age', 0),
            'salary': acc['salary'] + curr.get('salary', 0)
        },
        a_dictionary,
        {'age': 0, 'salary': 0}
    )

    n = len(a_dictionary)
    return (somas['salary'] / n, somas['age'] / n)