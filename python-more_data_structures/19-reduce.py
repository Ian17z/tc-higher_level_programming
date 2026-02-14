#!/usr/bin/python3
from functools import reduce

def calc_average(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return 0, 0  # Retornar algo consistente

    # Extrair valores ou 0 se não existir
    age = a_dictionary.get("age", 0)
    salary = a_dictionary.get("salary", 0)

    # Usando reduce para somar os dois valores
    total = reduce(lambda x, y: x + y, [age, salary])
    average = total / 2

    print(f"The average salary is R${salary:.2f} with an average age of {age:.2f}")
    return salary, age
