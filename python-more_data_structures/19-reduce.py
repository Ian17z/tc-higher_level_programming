#!/usr/bin/python3
#!/usr/bin/env python3
"""
Módulo com função para calcular médias usando reduce
"""

from functools import reduce

def calc_average(data):
    """
    Calcula a média dos salários e idades de uma lista de dicionários
    
    Args:
        data: Lista de dicionários contendo 'salary' e 'age'
        
    Returns:
        tuple: (média_salary, média_age)
    """
    if not data:
        return (0, 0)
    
    # Usando reduce para somar salários e idades
    totals = reduce(
        lambda acc, person: (acc[0] + person['salary'], acc[1] + person['age']),
        data,
        (0, 0)
    )
    
    # Calculando as médias
    n = len(data)
    average_salary = totals[0] / n
    average_age = totals[1] / n
    
    return (average_salary, average_age)


# Teste quando executado diretamente
if __name__ == "__main__":
    data = [
        {'name': 'Alice', 'age': 50, 'salary': 5000},
        {'name': 'Bob', 'age': 30, 'salary': 7000},
        {'name': 'Charlie', 'age': 35, 'salary': 9000},
        {'name': 'Dave', 'age': 40, 'salary': 11000},
    ]
    
    average_salary, average_age = calc_average(data)
    print(f'The average salary is R${average_salary:0.2f} with an average age of {average_age}')